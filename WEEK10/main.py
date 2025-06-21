# Main program for the Car Rental System
import os
from models import initialize_database, update_database_schema
from user_management import UserAuthentication
from customer_management import CustomerManagement
from admin_management import AdminManagement
from car_management import CarManagement
from rental_system import RentalSystem


def get_input(prompt):
    """Get input from console with error handling"""
    try:
        print(prompt, end='', flush=True)
        return input().strip()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return None
    except EOFError:
        print("\nInput error occurred.")
        return None


def get_password(prompt):
    """Get password input securely from console"""
    print(prompt, end='', flush=True)
    return input().strip()  # For simplicity, not hiding password


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print the application header"""
    print("\n" + "=" * 60)
    print("           🚘 CAR RENTAL SYSTEM 🚘")
    print("=" * 60)
    print("         New Zealand Best Car Rental System ")
    print("-" * 60)


def print_main_menu():
    print("\n=== 🏠 MAIN MENU ===")
    print("1. 📝 Register New User")
    print("2. 🔑 Login")
    print("3. 🚪 Exit")
    print("=" * 45)
    print("💡 Select an option to continue...")


def print_login_menu():
    print("\n=== 🔐 LOGIN PORTAL ===")
    print("1. 👑 Admin Login")
    print("2. 🧑 Customer Login")
    print("3. 🔓 Request Account Unlock")
    print("4. ↩️  Return")
    print("=" * 35)
    print("💡 Choose your login type...")


def print_admin_menu():
    print("\n=== 👑 ADMIN MENU ===")
    print("\n🚗 CAR MANAGEMENT")
    print("1. View & Manage Cars")
    print("2. Add New Car")
    
    print("\n👥 CUSTOMER MANAGEMENT")
    print("3. View & Manage Customers")
    print("4. Unlock Requests")
    
    print("\n📋 RENTAL MANAGEMENT")
    print("5. Rental Management")
    print("6. Booking Requests")
    
    print("\n⚙️  SYSTEM")
    print("7. System Statistics")
    print("8. Account Settings")
    print("9. Logout")
    print("=" * 25)


def print_customer_menu():
    print("\n=== 👤 CUSTOMER MENU ===")
    print("1. 🚗 View & Book Cars")
    print("2. 📋 My Rentals")
    print("3. 📝 Manage Bookings")
    print("4. ⚙️  Account Settings")
    print("5. 🚪 Logout")
    print("="*20)


def print_account_menu():
    print("\n=== ⚙️  ACCOUNT MANAGEMENT ===")
    print("1. 🔑 Change Password")
    print("2. 🔒 Update Security Question")
    print("3. ↩️  Back to Menu")
    print("="*25)


def print_table_separator(width=50):
    """Print a simple table separator line"""
    print("-" * width)


def print_section_header(title):
    """Print a simple section header"""
    print(f"\n=== {title} ===")


def format_rental_period(min_days, max_days):
    """Format rental period in a consistent way"""
    # Right-align min, left-align max for better readability
    return f"{min_days:>2}-{max_days:<2}"


def format_table_row(columns, values):
    """Format a table row with simple spacing"""
    # Simple format parts with adjusted widths
    fmt_parts = [
        "{:<4}",      # ID
        "{:<15}",     # Car/Username
        "{:<25}",     # Name/Customer
        "{:<15}",     # Phone/Email
        "{:<25}",     # Address
        "{:<8}",      # Days
        "{:<10}",     # Amount
        "{:<12}"      # Status
    ]
    
    # Join with simple separator
    fmt = " | ".join(fmt_parts[:columns])
    return fmt.format(*[str(v) for v in values])


def get_table_width():
    """Calculate total table width including separators"""
    # Column widths
    widths = [4, 12, 18, 20, 12, 18, 10, 8]
    # Add separators width: " | " between each column (3 chars * (n-1) columns)
    separators_width = 3 * (len(widths) - 1)
    # Total width is sum of all column widths plus separators
    return sum(widths) + separators_width


def print_table_header():
    """Print the car details table header"""
    print("\n=== 🚗 AVAILABLE CARS ===")
    print("-" * 50)
    print("ID   Make         Model        Year    Rate    Status")
    print("-" * 50)


def print_rental_header(show_customer=True):
    """Print a simple rental table header"""
    if show_customer:
        header_parts = [
            "ID", "Car", "Customer", "Phone",
            "Address", "Days", "Amount", "Status"
        ]
        print_section_header("RENTAL DETAILS")
    else:
        header_parts = [
            "ID", "Car", "Dates", "Days",
            "Amount", "Status"
        ]
        print_section_header("RENTAL HISTORY")
    
    print(format_table_row(len(header_parts), header_parts))
    print("=" * 120)  # Extended separator line


def format_rental_row(rental_data, show_customer=True):
    """Format rental data into a simple table row"""
    # Basic formatting
    car_name = rental_data['car'][:15]  # Increased width
    days = str(int(rental_data['rental_days']))
    
    # Get payment amount (try both field names)
    if 'total_cost' in rental_data:
        payment = rental_data['total_cost']
    elif 'total_amount' in rental_data:
        payment = rental_data['total_amount']
    else:
        payment = 0
    amount = f"${float(payment):.2f}"
    
    status = rental_data['status'][:10]  # Increased width
    
    if show_customer:
        # Get customer details from rental data
        user_id = rental_data.get('user_id')
        auth = UserAuthentication()
        customer = auth.get_customer_details(user_id) if user_id else None
        
        # Format name with first and last
        if customer:
            first = customer.get('first_name', '')
            last = customer.get('last_name', '')
            name = f"{first} {last}"[:25]  # Increased width
            phone = customer.get('phone_number', 'Not provided')
            address = customer.get('address', 'Not provided')
        else:
            # Fallback to rental data if customer details not found
            first = rental_data.get('first_name', '')
            last = rental_data.get('last_name', '')
            name = f"{first} {last}"[:25]  # Increased width
            phone = rental_data.get('phone_number', 'Not provided')
            address = rental_data.get('address', 'Not provided')
        
        # Format contact info
        phone = phone[:15]  # Increased width
        address = address[:25]  # Increased width
        
        values = [
            rental_data['rental_id'],
            car_name,
            name,
            phone,
            address,
            days,
            amount,
            status
        ]
    else:
        # Format dates
        start = rental_data['start_date'][:10]
        end = rental_data['end_date'][:10]
        dates = f"{start}-{end}"
        
        values = [
            rental_data['rental_id'],
            car_name,
            dates,
            days,
            amount,
            status
        ]
    
    return format_table_row(len(values), values)


def print_rental_list(rentals, show_customer=True):
    """Print a list of rentals in a formatted table"""
    if not rentals:
        print("\nNo rentals found.")
        return
    
    # Define column widths
    col_widths = {
        'id': 5,          # ID
        'car': 20,        # Car name
        'customer': 20,   # Customer name
        'phone': 15,      # Phone
        'address': 25,    # Address
        'days': 6,        # Days
        'amount': 12,     # Amount
        'status': 20      # Status - increased width
    }
    
    # Calculate total width including separators
    total_width = (
        sum(col_widths.values()) +  # Sum of all column widths
        (len(col_widths) * 3) - 1   # Account for ' | ' separators
    )
    
    print("\n" + "=" * total_width)
    print(f"{'📋 RENTAL DETAILS 📋':^{total_width}}")
    print("=" * total_width)
    
    # Print header based on view type
    if show_customer:
        header = (
            f"{'ID':^{col_widths['id']}} | "
            f"{'Car':<{col_widths['car']}} | "
            f"{'Customer':<{col_widths['customer']}} | "
            f"{'Phone':<{col_widths['phone']}} | "
            f"{'Address':<{col_widths['address']}} | "
            f"{'Days':^{col_widths['days']}} | "
            f"{'Amount':^{col_widths['amount']}} | "
            f"{'Status':<{col_widths['status']}}"
        )
    else:
        header = (
            f"{'ID':^{col_widths['id']}} | "
            f"{'Car':<{col_widths['car']}} | "
            f"{'Start Date':<15} | "
            f"{'End Date':<15} | "
            f"{'Days':^{col_widths['days']}} | "
            f"{'Amount':^{col_widths['amount']}} | "
            f"{'Status':<{col_widths['status']}}"
        )
    
    print("\n" + header)
    print("-" * total_width)
    
    # Print each rental
    for rental in rentals:
        # Format car name
        car_name = rental['car'][:col_widths['car']].strip()
        
        # Get payment amount
        if 'total_cost' in rental:
            payment = rental['total_cost']
        elif 'total_amount' in rental:
            payment = rental['total_amount']
        else:
            payment = 0
        amount = f"${float(payment):,.2f}"
        
        # Format days and status
        days = str(int(rental['rental_days']))
        status = print_rental_status_emoji(rental['status'])
        
        if show_customer:
            # Get customer details
            user_id = rental.get('user_id')
            auth = UserAuthentication()
            customer = auth.get_customer_details(user_id) if user_id else None
            
            # Format customer info
            if customer:
                first = customer.get('first_name', '')
                last = customer.get('last_name', '')
                name = f"{first} {last}"
                phone = customer.get('phone_number', 'Not provided')
                address = customer.get('address', 'Not provided')
            else:
                name = "N/A"
                phone = "Not provided"
                address = "Not provided"
            
            # Trim fields to fit columns
            name = name[:col_widths['customer']].strip()
            phone = phone[:col_widths['phone']].strip()
            address = address[:col_widths['address']].strip()
            
            # Print customer view row
            row = (
                f"{rental['rental_id']:^{col_widths['id']}} | "
                f"{car_name:<{col_widths['car']}} | "
                f"{name:<{col_widths['customer']}} | "
                f"{phone:<{col_widths['phone']}} | "
                f"{address:<{col_widths['address']}} | "
                f"{days:^{col_widths['days']}} | "
                f"{amount:>{col_widths['amount']}} | "
                f"{status:<{col_widths['status']}}"
            )
        else:
            # Format dates for history view
            start = rental['start_date'][:10]
            end = rental['end_date'][:10]
            
            # Print history view row
            row = (
                f"{rental['rental_id']:^{col_widths['id']}} | "
                f"{car_name:<{col_widths['car']}} | "
                f"{start:<15} | "
                f"{end:<15} | "
                f"{days:^{col_widths['days']}} | "
                f"{amount:>{col_widths['amount']}} | "
                f"{status:<{col_widths['status']}}"
            )
        
        print(row)
    
    print("-" * total_width)
    print(f"\nTotal Rentals: {len(rentals)}")
    print("=" * total_width)


def format_rental_status(status):
    """Format rental status with detailed icons and consistent descriptions"""
    status_icons = {
        'pending': '⏳ PENDING   (Awaiting Approval)',
        'approved': '✅ APPROVED  (Ready for Pickup)',
        'active': '🚗 ACTIVE    (Currently Rented)',
        'completed': '🏁 COMPLETED (Rental Finished)',
        'cancelled': '❌ CANCELLED (Booking Cancelled)',
        'rejected': '⛔ REJECTED  (Booking Denied)',
        'overdue': '⚠️ OVERDUE   (Past Due Date)',
        'reserved': '📅 RESERVED  (Future Booking)',
        'maintenance': '🔧 SERVICE   (Under Maintenance)'
    }
    return status_icons.get(status.lower(), status)


def print_rental_status_emoji(status):
    """Get emoji and short status for compact display"""
    status_icons = {
        'pending': '⏳ PENDING',
        'approved': '✅ APPROVED',
        'active': '🚗 ACTIVE',
        'completed': '🏁 COMPLETED',
        'cancelled': '❌ CANCELLED',
        'rejected': '⛔ REJECTED',
        'overdue': '⚠️ OVERDUE',
        'reserved': '📅 RESERVED',
        'maintenance': '🔧 SERVICE'
    }
    return status_icons.get(status.lower(), status)


def print_car_status(car):
    """Print detailed car status"""
    status_lines = []
    
    # Availability
    is_available = car.get('available', 1)
    if is_available:
        status_lines.append("✅ Available for Rent")
    else:
        status_lines.append("🚫 Currently Rented")
    
    # Rental Period
    min_days = car['min_rental_days']
    max_days = car['max_rental_days']
    status_lines.append(f"📅 Rental Period: {min_days}-{max_days} days")
    
    # Price Info
    rate = car['daily_rate']
    status_lines.append(f"💰 Rate: ${rate:.2f}/day")
    
    # Mileage Info
    mileage = car['mileage']
    status_lines.append(f"🛣️ Mileage: {mileage:,} km")
    
    return status_lines


def print_car_row(car, rental_sys=None, is_last=False):
    """Print a single car row with enhanced formatting"""
    # Get status
    status = "✅ Available" if car.get('available', 1) else "⛔ Rented"
    
    # Format basic info
    car_id = f"{car['car_id']:<4}"
    make = f"{car['make']:<12}"
    model = f"{car['model']:<12}"
    year = f"{car['year']:<7}"
    rate = f"${car['daily_rate']:<6.2f}"
    
    # Print basic info in table format
    print(f"{car_id}{make}{model}{year}{rate}{status}")
    
    # Print detailed info in a clean format
    print(f"   • Plate:    {car['plate_number']}")
    print(f"   • Mileage:  {car['mileage']:,} km")
    rental_days = f"{car['min_rental_days']}-{car['max_rental_days']}"
    print(f"   • Rental:   {rental_days} days")
    
    # Show rental details if car is rented
    if rental_sys and not car.get('available', 1):
        rental = rental_sys.get_rental_details(car['car_id'])
        if rental:
            print("\n   📋 Current Rental:")
            print(f"      • Customer: {rental['username']}")
            phone = rental.get('phone', 'Not provided')
            print(f"      • Phone:    {phone}")
            print(f"      • Period:   {rental['rental_days']} days")
    
    if not is_last:  # Only print separator if not last car
        print("-" * 50)


def print_rental_details(rental):
    """Print rental details with enhanced formatting"""
    if not rental or not rental.get('username'):
        return
    
    print("\n" + "=" * 50)
    print(f"        📋 RENTAL #{rental['rental_id']} 📋")
    print("=" * 50)
    
    # Customer Info
    print("\n👤 CUSTOMER INFORMATION")
    print("-" * 40)
    print(f"   • Name:          {rental.get('username', 'N/A')}")
    print(f"   • Phone:         {rental.get('phone', 'Not provided')}")
    
    # Rental Period
    print("\n📅 RENTAL PERIOD")
    print("-" * 40)
    print(f"   • Start Date:    {rental.get('start_date', 'N/A')}")
    print(f"   • End Date:      {rental.get('end_date', 'N/A')}")
    print(f"   • Duration:      {rental.get('rental_days', 0)} days")
    
    # Payment Info
    print("\n💳 PAYMENT DETAILS")
    print("-" * 40)
    print(f"   • Total Amount:  ${rental.get('total_cost', 0):.2f}")
    
    # Status
    status = format_rental_status(rental.get('status', 'N/A'))
    print("\n🔄 RENTAL STATUS")
    print("-" * 40)
    print(f"   • Status:        {status}")
    
    print("\n" + "=" * 50)


def print_success(message):
    """Print success message with celebration emoticons"""
    print(f"\n🎉 Success! {message} 🎊")


def print_error(message):
    """Print error message with warning emoticons"""
    print(f"\n⚠️  Error: {message} ❌")


def print_warning(message):
    """Print warning message with caution emoticons"""
    print(f"\n⚠️  Warning: {message} ⚠️")


def print_info(message):
    """Print info message with info emoticons"""
    print(f"\n💡 Info: {message}")


def handle_error(error_msg):
    """Handle errors with visual feedback"""
    print_error(error_msg)
    print("💡 Need help? Contact support or try again")
    return get_input("\n↩️  Press Enter to continue...")


def print_customer_table_header():
    """Print the customer details table header"""
    header_parts = [
        "ID   ",
        "Username      ",
        "Name                 ",
        "Email               ",
        "Phone          ",
        "Address             ",
        "License       ",
        "Status"
    ]
    header = " | ".join(header_parts)
    print("\n" + header)
    print_table_separator(120)


def format_customer_row(customer):
    """Format customer data into a table row"""
    # Format full name
    first = customer.get('first_name', '')
    last = customer.get('last_name', '')
    full_name = f"{first} {last}"
    
    # Format status
    status = "🔒 Locked" if customer.get('account_locked', 0) else "✅ Active"
    
    # Format row parts separately to avoid long lines
    row_parts = [
        "{id:<4}",
        "{username:<12}",
        "{name:<19}",
        "{email:<18}",
        "{phone:<13}",
        "{address:<18}",
        "{license:<12}",
        "{status:<6}"
    ]
    row_fmt = " | ".join(row_parts)
    
    return row_fmt.format(
        id=customer['user_id'],
        username=customer['username'][:12],
        name=full_name[:19],
        email=customer['email'][:18],
        phone=customer.get('phone_number', 'N/A')[:13],
        address=customer.get('address', 'N/A')[:18],
        license=customer.get('license_number', 'N/A')[:12],
        status=status
    )


def print_customer_details(customer):
    """Print detailed customer information"""
    print("\n" + "=" * 60)
    print("           👤 CUSTOMER DETAILS 👤")
    print("=" * 60)
    
    # Basic Info
    print("\n📋 BASIC INFORMATION")
    print("-" * 40)
    print(f"   • ID:         {customer['user_id']}")
    print(f"   • Username:   {customer['username']}")
    name = f"{customer.get('first_name', '')} {customer.get('last_name', '')}"
    print(f"   • Name:       {name}")
    print(f"   • Email:      {customer.get('email', 'Not set')}")
    
    # Contact Info
    print("\n📞 CONTACT INFORMATION")
    print("-" * 40)
    print(f"   • Phone:      {customer.get('phone_number', 'Not set')}")
    print(f"   • Address:    {customer.get('address', 'Not set')}")
    print(f"   • License:    {customer.get('license_number', 'Not set')}")
    
    # Account Status
    print("\n🔐 ACCOUNT STATUS")
    print("-" * 40)
    is_locked = customer.get('account_locked')
    status = "🔒 LOCKED" if is_locked else "🔓 UNLOCKED"
    print(f"   • Status:     {status}")
    print(f"   • Attempts:   {customer.get('login_attempts', 0)} login attempts")
    
    # Action Menu
    print("\n⚡ AVAILABLE ACTIONS")
    print("-" * 40)
    print("1. 🔒 LOCK ACCOUNT   - Prevent customer from logging in")
    print("2. 🔓 UNLOCK ACCOUNT - Restore customer's access")
    print("3. ↩️  BACK         - Return to previous menu")
    print("\n" + "=" * 60)
    print("💡 Enter 1 to lock, 2 to unlock, or 3 to go back")


def handle_customer_details(auth, admin_mgmt, customer_id):
    """Handle customer details view and actions"""
    while True:
        customer = auth.get_customer_details(customer_id)
        if not customer:
            print_error("Customer not found")
            return

        print_customer_details(customer)
        choice = get_input("Enter choice (1-3): ")

        if choice == '3' or not choice:  # Back
            break
        elif choice in ['1', '2']:  # Lock/Unlock
            action = 'lock' if choice == '1' else 'unlock'
            
            # Confirm action
            confirm = get_input(f"Confirm {action} account? (y/n): ").lower()
            if confirm != 'y':
                print_info("Action cancelled")
                continue
            
            # Add admin notes
            notes = get_input("Enter admin notes (optional): ")
            
            # Perform action
            success, message = admin_mgmt.manage_customer_account(customer_id, action)
            if success:
                print_success(message)
            else:
                print_error(message)
        
        get_input("\nPress Enter to continue...")


def print_customer_list(customers):
    """Print customer list with enhanced visual feedback"""
    if not customers:
        print_info("No customers registered in the system")
        return
    
    print_section_header("📋 CUSTOMER DIRECTORY")
    print(f"Total Customers: {len(customers)}")
    print("-" * 50)
    
    for customer in customers:
        # Format name
        first = customer.get('first_name', '')
        last = customer.get('last_name', '')
        name = f"{first} {last}".strip() or "N/A"
        
        # Format status with icon
        is_locked = customer.get('account_locked')
        status = "🔒" if is_locked else "✅"
        
        # Print customer entry
        print(f"\n👤 Customer #{customer['user_id']}:")
        print(f"   📝 Name: {name}")
        print(f"   🔑 User: {customer['username']}")
        print(f"   📧 Email: {customer['email']}")
        print(f"   📱 Phone: {customer.get('phone_number', 'N/A')}")
        print(f"   🔄 Status: {status}")
        print("-" * 40)


def print_search_menu():
    """Print the simplified search menu"""
    print("\n=== 🔍 CUSTOMER SEARCH ===")
    print("1. 👤 Search by Name")
    print("2. 📧 Search by Email")
    print("3. 📱 Search by Phone")
    print("4. ↩️  Back")
    print("\n💡 Tip: You can enter partial text to search")
    print("=" * 30)


def print_search_results(results):
    """Print search results in a simple format"""
    if not results:
        print("\n❌ No customers found.")
        print("💡 Tip: Try entering less text to find more matches")
        return
    
    print(f"\n✨ Found {len(results)} customer(s):")
    print("-" * 30)
    
    for customer in results:
        # Get name parts
        first = customer.get('first_name', '')
        last = customer.get('last_name', '')
        name = f"{first} {last}"
        
        # Format status more clearly
        is_locked = customer.get('account_locked')
        status = "⛔ [LOCKED]" if is_locked else "✅ [ACTIVE]"
        
        # Print customer info with icons
        print(f"\n🆔 ID: {customer['user_id']}")
        print(f"👤 Name: {name.strip()}")
        print(f"📧 Email: {customer.get('email', 'N/A')}")
        print(f"📱 Phone: {customer.get('phone_number', 'N/A')}")
        print(f"🔄 Status: {status}")
        print("-" * 30)


def handle_customer_search(auth, admin_mgmt):
    """Handle customer search with simplified options"""
    while True:
        print_search_menu()
        choice = get_input("Enter choice (1-4): ")
        
        if not choice or choice == '4':
            return
        
        search_fields = {
            '1': ('name', "Enter name to search: "),
            '2': ('email', "Enter email to search: "),
            '3': ('phone', "Enter phone to search: ")
        }
        
        if choice in search_fields:
            field, prompt = search_fields[choice]
            term = get_input(prompt)
            
            if term:
                print(f"\nSearching for '{term}'...")
                results = auth.search_customers(term)
                print_search_results(results)
                
                if results:
                    while True:
                        prompt = "\nView details (ID) or press Enter: "
                        action = get_input(prompt)
                        if not action:
                            break
                        
                        if action.isdigit():
                            handle_customer_details(auth, admin_mgmt, int(action))
                            break
            
            get_input("\nPress Enter to continue...")


def print_customer_management_menu():
    """Print the customer management menu"""
    print("\n=== 👥 CUSTOMER MANAGEMENT ===")
    print("1. 📋 View All Customers")
    print("2. 🔍 Search Customers")
    print("3. 👤 View Customer Details")
    print("4. ↩️  Back to Admin Menu")
    print("=" * 25)


def print_system_stats(stats):
    """Print system statistics with enhanced formatting"""
    if not stats:
        print_error("Could not retrieve system statistics")
        return
    
    print("\n" + "=" * 60)
    print("           📊 SYSTEM DASHBOARD 📊")
    print("=" * 60)
    
    # Customer Overview
    print("\n👥 CUSTOMER OVERVIEW")
    print("-" * 40)
    total = stats['total_customers']
    active = stats['active_customers']
    print(f"   • Total Customers:  {total:>4}")
    print(f"   • Currently Active: {active:>4}")
    
    # Rental Overview
    print("\n🚗 RENTAL OVERVIEW")
    print("-" * 40)
    current = stats['current_rentals']
    completed = stats['completed_rentals']
    print(f"   • Current Rentals:  {current:>4}")
    print(f"   • Completed:        {completed:>4}")
    
    # Business Overview
    print("\n💰 BUSINESS OVERVIEW")
    print("-" * 40)
    revenue = stats['total_revenue']
    avg_revenue = revenue / completed if completed > 0 else 0
    print(f"   • Total Revenue:    ${revenue:>7.2f}")
    print(f"   • Avg. per Rental:  ${avg_revenue:>7.2f}")
    
    print("\n" + "=" * 60)


def print_unlock_requests(requests):
    """Print unlock requests with visual feedback"""
    if not requests:
        print_info("No pending unlock requests")
        return
    
    print_section_header("🔓 UNLOCK REQUESTS")
    print(f"Pending Requests: {len(requests)}")
    print("-" * 50)
    
    for req in requests:
        print(f"\n📝 Request #{req['request_id']}:")
        print(f"   👤 User: {req['username']}")
        reason = req['reason']
        # Split long reason text into multiple lines if needed
        if len(reason) > 40:
            print("   📄 Reason:")
            print(f"      {reason}")
        else:
            print(f"   📄 Reason: {reason}")
        print("-" * 40)


def handle_admin_menu(auth, admin_mgmt, car_mgmt, rental_sys, user_data):
    while True:
        print_admin_menu()
        choice = get_input("Enter your choice (1-9): ")
        
        if not choice:  # Handle cancelled input
            continue
        
        if choice == '9':  # Logout
            break
        
        elif choice == '1':  # View & Manage Cars
            handle_car_management(car_mgmt, rental_sys)
        elif choice == '2':  # Add New Car
            make = get_input("Enter car make: ")
            model = get_input("Enter car model: ")
            try:
                year = int(get_input("Enter car year: "))
                plate = get_input("Enter plate number: ")
                rate = float(get_input("Enter daily rate: "))
                mileage = float(get_input("Enter mileage: "))
                min_days = int(get_input("Enter minimum rental days: "))
                max_days = int(get_input("Enter maximum rental days: "))
                success, message = car_mgmt.add_car(
                    make, model, year, plate, mileage, rate,
                    min_rental_days=min_days, max_rental_days=max_days
                )
                print(message)
            except ValueError:
                print("\nError: Please enter valid numeric values")
        elif choice == '3':  # View & Manage Customers
            while True:
                print_customer_management_menu()
                sub_choice = get_input("Enter choice (1-4): ")
                
                if not sub_choice:  # Handle cancelled input
                    continue
                
                if sub_choice == '1':  # View All
                    customers = auth.get_all_customers()
                    if customers:
                        print_customer_list(customers)
                    else:
                        print_info("No customers registered")
                
                elif sub_choice == '2':  # Search
                    handle_customer_search(auth, admin_mgmt)
                
                elif sub_choice == '3':  # View Details
                    try:
                        prompt = "\nEnter customer ID (or Enter to cancel): "
                        cust_id = get_input(prompt)
                        
                        if cust_id and cust_id.isdigit():
                            cust_id = int(cust_id)
                            handle_customer_details(auth, admin_mgmt, cust_id)
                    except ValueError:
                        msg = "Please enter a valid customer ID"
                        print_error(msg)
                
                elif sub_choice == '4':  # Back
                    break
                
                if sub_choice != '4':
                    prompt = "\nPress Enter to continue or 'b' to go back: "
                    if get_input(prompt).lower() == 'b':
                        break
        elif choice == '4':  # Unlock Requests
            requests = auth.get_unlock_requests(user_data['user_id'])
            if requests:
                print_unlock_requests(requests)
                
                try:
                    prompt = "\nEnter request ID (0 to cancel): "
                    req_id = int(get_input(prompt))
                    if req_id != 0:
                        action = get_input("Approve? (y/n): ").lower()
                        notes = get_input("Admin notes: ")
                        success, message = auth.handle_unlock_request(
                            req_id,
                            user_data['user_id'],
                            approve=(action == 'y'),
                            admin_notes=notes
                        )
                        print(message)
                except ValueError:
                    print_error("Please enter a valid request ID")
            else:
                print_info("No pending unlock requests")
        elif choice == '5':  # Rental Management
            handle_rental_management(rental_sys, auth, user_data)
        elif choice == '6':  # Booking Requests
            handle_booking_requests(rental_sys, auth, user_data)
        elif choice == '7':  # System Statistics
            stats = admin_mgmt.get_system_stats()
            if stats:
                print_system_stats(stats)
            else:
                print_error("Could not retrieve system statistics")
        elif choice == '8':  # Account Settings
            while True:
                print_account_menu()
                account_choice = get_input("Enter your choice (1-3): ")
                
                if account_choice == '1':  # Change Password
                    current_pwd = get_password("Enter current password: ")
                    new_pwd = get_password("Enter new password: ")
                    confirm_pwd = get_password("Confirm new password: ")
                    
                    if new_pwd != confirm_pwd:
                        print("\nError: Passwords do not match!")
                    else:
                        success, message = auth.change_password(
                            user_data['user_id'],
                            current_pwd,
                            new_pwd
                        )
                        print(f"\n{message}")
                
                elif account_choice == '2':  # Update Security Question
                    question = get_input("Enter new security question: ")
                    answer = get_input("Enter new security answer: ")
                    success, message = auth.update_security_question(
                        user_data['user_id'],
                        question,
                        answer
                    )
                    print(f"\n{message}")
                
                elif account_choice == '3':  # Back to Admin Menu
                    break
                
                if account_choice != '3':
                    get_input("\nPress Enter to continue...")
        
        if choice != '9':
            input_result = get_input("\nPress Enter to continue...")
            if not input_result:  # Handle cancelled input
                continue


def print_customer_account_menu():
    """Print the customer account settings menu"""
    print("\n=== ⚙️  ACCOUNT SETTINGS ===")
    print("1. 👀 View Profile")
    print("2. 👤 Update Profile")
    print("3. 🔑 Change Password")
    print("4. ↩️  Back to Menu")
    print("=" * 25)


def print_customer_profile(customer):
    """Print customer profile details in a formatted way"""
    print("\n" + "=" * 50)
    print("           👤 MY PROFILE 👤")
    print("=" * 50)
    
    # Personal Info
    print("\n📋 PERSONAL INFORMATION")
    print("-" * 40)
    first = customer.get('first_name', '')
    last = customer.get('last_name', '')
    name = f"{first} {last}".strip() or "Not provided"
    print(f"   • Name:       {name}")
    print(f"   • Username:   {customer['username']}")
    print(f"   • Email:      {customer['email']}")
    
    # Contact Info
    print("\n📞 CONTACT DETAILS")
    print("-" * 40)
    phone = customer.get('phone_number', 'Not provided')
    addr = customer.get('address', 'Not provided')
    print(f"   • Phone:      {phone}")
    print(f"   • Address:    {addr}")
    
    # License Info
    print("\n🚗 DRIVER INFORMATION")
    print("-" * 40)
    license_num = customer.get('license_number', 'Not provided')
    print(f"   • License:    {license_num}")
    
    print("\n" + "=" * 50)


def handle_customer_account_settings(auth, user_data):
    """Handle customer account settings menu"""
    while True:
        print_customer_account_menu()
        choice = get_input("Enter your choice (1-4): ")
        
        if choice == '4':  # Back to Menu
            break
            
        elif choice == '1':  # View Profile
            # Get current details
            current = auth.get_customer_details(user_data['user_id'])
            if current:
                print_customer_profile(current)
            else:
                print_error("Could not retrieve profile details")
            
        elif choice == '2':  # Update Profile
            print("\n=== 👤 UPDATE PROFILE ===")
            print("Leave blank to keep current value")
            
            # Get current details
            current = auth.get_customer_details(user_data['user_id'])
            if not current:
                print_error("Could not retrieve current profile")
                continue
            
            # Get new values
            first_name = current.get('first_name', '')
            last_name = current.get('last_name', '')
            phone = current.get('phone_number', 'Not set')
            address = current.get('address', 'Not set')
            license_num = current.get('license_number', 'Not set')
            
            # Get user input with current values shown
            first = get_input(f"First Name [{first_name}]: ")
            last = get_input(f"Last Name [{last_name}]: ")
            new_phone = get_input(f"Phone [{phone}]: ")
            new_addr = get_input(f"Address [{address}]: ")
            new_license = get_input(f"License [{license_num}]: ")
            
            # Build updates dict
            updates = {}
            if first:
                updates['first_name'] = first
            if last:
                updates['last_name'] = last
            if new_phone:
                updates['phone_number'] = new_phone
            if new_addr:
                updates['address'] = new_addr
            if new_license:
                updates['license_number'] = new_license
            
            if updates:
                success, msg = auth.update_customer_profile(
                    user_data['user_id'],
                    **updates
                )
                if success:
                    print_success(msg)
                else:
                    print_error(msg)
            else:
                print_info("No changes made")
                
        elif choice == '3':  # Change Password
            print("\n=== 🔑 CHANGE PASSWORD ===")
            current = get_password("Current Password: ")
            new = get_password("New Password: ")
            confirm = get_password("Confirm New Password: ")
            
            if new != confirm:
                print_error("New passwords do not match")
            else:
                success, msg = auth.change_password(
                    user_data['user_id'],
                    current,
                    new
                )
                if success:
                    print_success(msg)
                else:
                    print_error(msg)
        
        if choice != '4':
            get_input("\nPress Enter to continue...")


def handle_customer_menu(auth, customer_mgmt, car_mgmt, rental_sys, user_data):
    while True:
        print_customer_menu()
        choice = get_input("Enter your choice (1-5): ")
        
        if choice == '5':  # LOGOUT
            break
        elif choice == '1':  # View & Book Cars
            cars = car_mgmt.get_available_cars()
            if cars:
                print("\n=== 🚗 AVAILABLE CARS ===")
                print("-" * 50)
                print("ID   Make         Model        Year    Rate    Status")
                print("-" * 50)
                
                for i, car in enumerate(cars):
                    is_last = (i == len(cars) - 1)
                    print_car_row(car, rental_sys, is_last)
                
                try:
                    prompt = "\nEnter car ID to book (0 to cancel): "
                    car_id = int(get_input(prompt))
                    if car_id != 0:
                        # Get customer details for rental
                        cust = auth.get_customer_details(user_data['user_id'])
                        if not cust:
                            print_error("Customer details not found")
                            continue
                        
                        # Get rental dates
                        start = get_input("Start date (YYYY-MM-DD): ")
                        end = get_input("End date (YYYY-MM-DD): ")
                        
                        # Create rental
                        success, msg = rental_sys.create_rental(
                            user_data['user_id'],
                            car_id,
                            start,
                            end
                        )
                        if success:
                            print_success(msg)
                        else:
                            print_error(msg)
                except ValueError:
                    print_error("Please enter a valid car ID")
            else:
                print_info("No cars available for rent")
        
        elif choice == '2':  # My Rentals
            rentals = rental_sys.get_user_rentals(user_data['user_id'])
            if rentals:
                print("\nMy Rental History:")
                print_rental_list(rentals, show_customer=False)
            else:
                print_info("No rental history found")
        
        elif choice == '3':  # Manage Bookings
            handle_manage_bookings(auth, rental_sys, user_data)
            
        elif choice == '4':  # Account Settings
            handle_customer_account_settings(auth, user_data)
        
        if choice != '5':
            get_input("\nPress Enter to continue...")


def cleanup():
    """Clean up resources before exit"""
    try:
        # Get all instances that might have DB connections
        auth = UserAuthentication()
        customer_mgmt = CustomerManagement()
        admin_mgmt = AdminManagement()
        car_mgmt = CarManagement()
        rental_sys = RentalSystem()
        
        # Close their connections
        if hasattr(auth, 'conn') and auth.conn:
            auth.conn.close()
        if hasattr(customer_mgmt, 'conn') and customer_mgmt.conn:
            customer_mgmt.conn.close()
        if hasattr(admin_mgmt, 'conn') and admin_mgmt.conn:
            admin_mgmt.conn.close()
        if hasattr(car_mgmt, 'conn') and car_mgmt.conn:
            car_mgmt.conn.close()
        if hasattr(rental_sys, 'conn') and rental_sys.conn:
            rental_sys.conn.close()
    except Exception as e:
        print(f"Error during cleanup: {e}")
    finally:
        # Ensure we always exit cleanly
        pass


def main():
    try:
        # Initialize database and managers
        initialize_database()
        update_database_schema()
        auth = UserAuthentication()
        customer_mgmt = CustomerManagement()
        admin_mgmt = AdminManagement()
        car_mgmt = CarManagement()
        rental_sys = RentalSystem()
        
        while True:
            clear_screen()
            print_header()
            print_main_menu()
            choice = get_input("Enter your choice (1-3): ")
            
            if choice == '1':  # Register New User
                print("\n=== 📝 User Registration ===")
                username = get_input("Enter username: ")
                password = get_password("Enter password: ")
                email = get_input("Enter email: ")
                
                # Get required customer details
                print("\n👤 Personal Information:")
                first_name = get_input("First Name: ")
                last_name = get_input("Last Name: ")
                phone = get_input("Phone Number: ")
                address = get_input("Address: ")
                license_number = get_input("Driver's License: ")
                
                # Register with all details
                success, message = auth.register_user(
                    username, password, email, 'customer',
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone,
                    address=address,
                    license_number=license_number
                )
                print_success(message) if success else print_error(message)
                
            elif choice == '2':  # Login
                display_login_menu()
            
            elif choice == '3':  # Exit
                print("\nThank you for using the Car Rental System!")
                break
            
            if choice != '3':
                get_input("\nPress Enter to continue...")
    finally:
        cleanup()


def display_login_menu():
    """Display the login menu and handle user input"""
    while True:
        print("\n=== 🔐 LOGIN PORTAL ===")
        print("1. 👑 Admin Login")
        print("2. 🧑 Customer Login")
        print("3. 🔓 Request Account Unlock")
        print("4. ↩️  Return")
        print("===================================")
        
        print("💡 Choose your login type...")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            handle_admin_login()
        elif choice == '2':
            handle_customer_login()
        elif choice == '3':
            handle_unlock_request()
        elif choice == '4':
            return
        else:
            print("\n⚠️  Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


def handle_unlock_request():
    """Handle user's unlock request"""
    print("\n=== 🔓 REQUEST ACCOUNT UNLOCK ===")
    username = input("Enter your username: ")
    reason = input("Enter reason for unlock request: ")
    
    auth = UserAuthentication()
    success, message = auth.create_unlock_request(username, reason)
    
    if success:
        print("\n✅ " + message)
        print("An administrator will review your request shortly.")
    else:
        print("\n⚠️  " + message)


def handle_customer_login():
    """Handle customer login process"""
    print("\n=== 🧑 CUSTOMER LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    
    auth = UserAuthentication()
    success, result = auth.login(username, password)
    
    if success:
        print("\n✅ Login successful!")
        handle_customer_menu(
            auth, CustomerManagement(), CarManagement(),
            RentalSystem(), result
        )
    else:
        print(f"\n⚠️  Error: {result} ❌")
        
        # Check if account is locked and suggest unlock request
        if "account has been locked" in result.lower():
            print("\n💡 Your account is locked. You can:")
            print("1. Contact an administrator")
            print("2. Submit an unlock request")
            
            choice = input("\nWould you like to submit an unlock request now? (y/n): ")
            if choice.lower() == 'y':
                handle_unlock_request()


def handle_admin_login():
    """Handle admin login process"""
    print("\n=== 👑 ADMIN LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    
    auth = UserAuthentication()
    admin_mgmt = AdminManagement()
    car_mgmt = CarManagement()
    rental_sys = RentalSystem()
    success, result = auth.login(username, password)
    
    if success and isinstance(result, dict) and result.get('role') == 'admin':
        # Get admin security question
        success, question = admin_mgmt.get_security_question(result['user_id'])
        
        if success:
            print(f"\nSecurity Question: {question}")
            answer = input("Answer: ")
            verified = admin_mgmt.verify_security_answer(result['user_id'], answer)
            
            if verified:
                print("\n✅ Admin login successful!")
                handle_admin_menu(auth, admin_mgmt, car_mgmt, rental_sys, result)
            else:
                print("\n⚠️  Incorrect security answer")
        else:
            print("\n⚠️  Error retrieving security question")
    else:
        print("\n⚠️  Invalid admin credentials")


def print_rental_reports_menu():
    """Print the rental reports menu"""
    print("\n=== 📈 RENTAL REPORTS ===")
    print("1. 📊 View All Rentals Report")
    print("2. 👤 Customer Specific Report")
    print("3. 📅 Date Range Report")
    print("4. 🔍 Status Based Report")
    print("5. ↩️  Back to Admin Menu")
    print("=" * 25)


def print_rental_statistics(stats):
    """Print rental statistics in a formatted way"""
    if not stats:
        print_error("No statistics available")
        return
    
    print("\n" + "=" * 50)
    print("           📊 RENTAL STATISTICS 📊")
    print("=" * 50)
    
    # Rental Counts
    print("\n📋 RENTAL COUNTS")
    print("-" * 40)
    print(f"   • Total Rentals:     {stats['total_rentals']:>4}")
    print(f"   • Completed:         {stats['completed_rentals']:>4}")
    print(f"   • Active:            {stats['active_rentals']:>4}")
    print(f"   • Pending:           {stats['pending_rentals']:>4}")
    print(f"   • Cancelled:         {stats['cancelled_rentals']:>4}")
    
    # Financial Statistics
    print("\n💰 FINANCIAL OVERVIEW")
    print("-" * 40)
    revenue = stats['total_revenue'] or 0
    avg_revenue = stats['average_rental_cost'] or 0
    print(f"   • Total Revenue:     ${revenue:>8.2f}")
    print(f"   • Average Cost:      ${avg_revenue:>8.2f}")
    
    # Duration Statistics
    print("\n⏱️ DURATION STATISTICS")
    print("-" * 40)
    avg_days = stats['average_rental_days'] or 0
    print(f"   • Average Duration:  {avg_days:>8.1f} days")
    
    print("\n" + "=" * 50)


def print_detailed_rental_history(rentals):
    """Print detailed rental history in a formatted table"""
    if not rentals:
        print_info("No rental history found")
        return
    
    # Define column widths
    col_widths = {
        'id': 5,          # ID
        'customer': 20,   # Customer name
        'car': 20,        # Car details
        'dates': 25,      # Rental dates
        'days': 6,        # Rental days
        'amount': 12,     # Amount
        'status': 20      # Status - increased width
    }
    
    # Calculate total width including separators
    total_width = (
        sum(col_widths.values()) +  # Sum of all column widths
        (len(col_widths) * 3) - 1   # Account for ' | ' separators
    )
    
    print("\n" + "=" * total_width)
    print(f"{'📋 DETAILED RENTAL HISTORY 📋':^{total_width}}")
    print("=" * total_width)
    
    # Print header
    header = (
        f"{'ID':^{col_widths['id']}} | "
        f"{'Customer':<{col_widths['customer']}} | "
        f"{'Car':<{col_widths['car']}} | "
        f"{'Rental Period':<{col_widths['dates']}} | "
        f"{'Days':^{col_widths['days']}} | "
        f"{'Amount':^{col_widths['amount']}} | "
        f"{'Status':<{col_widths['status']}}"
    )
    print("\n" + header)
    print("-" * total_width)
    
    # Print each rental with proper formatting
    for rental in rentals:
        # Format customer name
        customer = f"{rental['first_name']} {rental['last_name']}"
        customer = customer[:col_widths['customer']].strip()
        
        # Format car info
        car = f"{rental['make']} {rental['model']}"
        car = car[:col_widths['car']].strip()
        
        # Format dates
        dates = f"{rental['start_date'][:10]} → {rental['end_date'][:10]}"
        dates = dates[:col_widths['dates']].strip()
        
        # Format other fields
        rental_id = str(rental['rental_id'])
        days = str(int(rental['rental_days']))
        amount = f"${rental['total_cost']:,.2f}"
        status = print_rental_status_emoji(rental['status'])
        
        # Print formatted row
        row = (
            f"{rental_id:^{col_widths['id']}} | "
            f"{customer:<{col_widths['customer']}} | "
            f"{car:<{col_widths['car']}} | "
            f"{dates:<{col_widths['dates']}} | "
            f"{days:^{col_widths['days']}} | "
            f"{amount:>{col_widths['amount']}} | "
            f"{status:<{col_widths['status']}}"
        )
        print(row)
    
    print("-" * total_width)
    print(f"\nTotal Rentals: {len(rentals)}")
    print("=" * total_width)


def handle_rental_reports(rental_sys, auth):
    """Handle the rental reports menu"""
    while True:
        print_rental_reports_menu()
        choice = get_input("Enter choice (1-5): ")
        
        if choice == '5':  # Back
            break
        
        elif choice == '1':  # All Rentals Report
            # Get and display statistics
            stats = rental_sys.get_rental_statistics()
            print_rental_statistics(stats)
            
            # Get and display detailed history
            rentals = rental_sys.get_rental_history_by_customer()
            print_detailed_rental_history(rentals)
            
        elif choice == '2':  # Customer Specific Report
            # Get customer ID
            username = get_input("\nEnter customer username: ")
            customer = auth.get_customer_details_by_username(username)
            
            if customer:
                # Get and display statistics
                stats = rental_sys.get_rental_statistics(customer['user_id'])
                print_rental_statistics(stats)
                
                # Get and display detailed history
                rentals = rental_sys.get_rental_history_by_customer(customer['user_id'])
                print_detailed_rental_history(rentals)
            else:
                print_error("Customer not found")
            
        elif choice == '3':  # Date Range Report
            # Get date range
            print("\nEnter date range (YYYY-MM-DD):")
            start_date = get_input("Start date: ")
            end_date = get_input("End date: ")
            
            # Get and display rentals for date range
            rentals = rental_sys.get_rental_history_by_customer(
                start_date=start_date,
                end_date=end_date
            )
            print_detailed_rental_history(rentals)
            
        elif choice == '4':  # Status Based Report
            # Show status options
            print("\nStatus Options:")
            print("1. Pending")
            print("2. Active")
            print("3. Completed")
            print("4. Cancelled")
            
            status_map = {
                '1': 'pending',
                '2': 'active',
                '3': 'completed',
                '4': 'cancelled'
            }
            
            status_choice = get_input("\nChoose status (1-4): ")
            if status_choice in status_map:
                status = status_map[status_choice]
                rentals = rental_sys.get_rental_history_by_customer(status=status)
                print_detailed_rental_history(rentals)
            else:
                print_error("Invalid status choice")
        
        if choice != '5':
            get_input("\nPress Enter to continue...")


def handle_car_management(car_mgmt, rental_sys):
    """Handle car management submenu"""
    while True:
        print("\n=== 🚗 CAR MANAGEMENT ===")
        print("1. View All Cars")
        print("2. Update Car")
        print("3. Delete Car")
        print("4. Back")
        
        choice = get_input("\nEnter choice (1-4): ")
        
        if choice == '4':  # Back
            break
            
        elif choice == '1':  # View All Cars
            cars = car_mgmt.get_all_cars()
            if cars:
                print("\nAll Cars:")
                print_table_header()
                for car in cars:
                    print_car_row(car, rental_sys)
                print(f"\nTotal Cars: {len(cars)}")
            else:
                print("\nNo cars in the system")
                
        elif choice == '2':  # Update Car
            cars = car_mgmt.get_all_cars()
            if cars:
                print("\nAvailable Cars:")
                print_table_header()
                for i, car in enumerate(cars):
                    is_last = (i == len(cars) - 1)
                    print_car_row(car, rental_sys, is_last)
                try:
                    car_id = int(get_input("\nEnter ID to update (0 to cancel): "))
                    if car_id != 0:
                        print("\nLeave blank to skip update")
                        make = get_input("New make: ")
                        model = get_input("New model: ")
                        year_str = get_input("New year: ")
                        plate = get_input("New plate: ")
                        rate_str = get_input("New rate: ")
                        mileage_str = get_input("New mileage: ")
                        min_days_str = get_input("New min rental days: ")
                        max_days_str = get_input("New max rental days: ")
                        
                        updates = {}
                        if make: updates['make'] = make
                        if model: updates['model'] = model
                        if year_str: updates['year'] = int(year_str)
                        if plate: updates['plate_number'] = plate
                        if rate_str: updates['daily_rate'] = float(rate_str)
                        if mileage_str: updates['mileage'] = float(mileage_str)
                        if min_days_str: updates['min_rental_days'] = int(min_days_str)
                        if max_days_str: updates['max_rental_days'] = int(max_days_str)
                        
                        if updates:
                            success, message = car_mgmt.update_car(car_id, **updates)
                            print(message)
                        else:
                            print("\nNo updates provided")
                except ValueError:
                    print("\nError: Please enter valid numeric values")
            else:
                print("\nNo cars available")
                
        elif choice == '3':  # Delete Car
            cars = car_mgmt.get_all_cars()
            if cars:
                print("\nAvailable Cars:")
                print_table_header()
                for car in cars:
                    print_car_row(car, rental_sys)
                try:
                    car_id = int(get_input("\nEnter ID to delete (0 to cancel): "))
                    if car_id != 0:
                        confirm = get_input("Delete? (y/n): ").lower()
                        if confirm == 'y':
                            success, message = car_mgmt.delete_car(car_id)
                            print(message)
                except ValueError:
                    print("\nError: Please enter a valid car ID")
            else:
                print("\nNo cars available")
        
        if choice != '4':
            get_input("\nPress Enter to continue...")


def handle_rental_management(rental_sys, auth, user_data):
    """Unified rental management function combining active rentals and reports"""
    while True:
        print("\n=== 📋 RENTAL MANAGEMENT ===")
        print("1. View Active Rentals")
        print("2. View All Rentals")
        print("3. Search by Customer")
        print("4. Search by Date Range")
        print("5. Search by Status")
        print("6. Back to Main Menu")
        print("=" * 30)
        
        choice = get_input("\nEnter choice (1-6): ")
        
        if choice == '6':  # Back
            break
            
        elif choice == '1':  # Active Rentals
            # Get active and pending rentals
            rentals = rental_sys.get_all_rentals(user_data['user_id'])
            active_rentals = [
                r for r in rentals 
                if r['status'] in ['active', 'approved', 'pending']
            ]
            
            if not active_rentals:
                print_info("No active rentals found")
                continue
                
            print("\nActive & Pending Rentals:")
            print_rental_list(active_rentals, show_customer=True)
            
            # Handle rental actions
            try:
                rental_id = int(get_input("\nEnter rental ID (0 to cancel): "))
                if rental_id != 0:
                    print("\nStatus Options:")
                    print("1. ✅ Approve Rental")
                    print("2. 🏁 Complete Rental")
                    print("3. ❌ Cancel Rental")
                    
                    status_choice = get_input("Choose (1-3): ")
                    status_map = {
                        '1': 'approved',
                        '2': 'completed',
                        '3': 'cancelled'
                    }
                    
                    if status_choice in status_map:
                        status = status_map[status_choice]
                        result = rental_sys.update_rental_status(
                            rental_id,
                            status,
                            user_data['user_id']
                        )
                        if result[0]:
                            print_success(result[1])
                        else:
                            print_error(result[1])
            except ValueError:
                print_error("Invalid rental ID")
                
        elif choice == '2':  # All Rentals
            # Get and display statistics
            stats = rental_sys.get_rental_statistics()
            print_rental_statistics(stats)
            
            # Get and display all rentals
            rentals = rental_sys.get_rental_history_by_customer()
            print_detailed_rental_history(rentals)
            
        elif choice == '3':  # Search by Customer
            username = get_input("\nEnter customer username: ")
            customer = auth.get_customer_details_by_username(username)
            
            if customer:
                # Get customer's rental history
                rentals = rental_sys.get_rental_history_by_customer(
                    customer['user_id']
                )
                if rentals:
                    print_detailed_rental_history(rentals)
                else:
                    print_info("No rentals found for this customer")
            else:
                print_error("Customer not found")
                
        elif choice == '4':  # Search by Date Range
            print("\nEnter date range (YYYY-MM-DD):")
            start_date = get_input("Start date: ")
            end_date = get_input("End date: ")
            
            rentals = rental_sys.get_rental_history_by_customer(
                start_date=start_date,
                end_date=end_date
            )
            if rentals:
                print_detailed_rental_history(rentals)
            else:
                print_info("No rentals found in this date range")
                
        elif choice == '5':  # Search by Status
            print("\nStatus Options:")
            print("1. ⏳ Pending Rentals")
            print("2. 🚗 Active Rentals")
            print("3. 🏁 Completed Rentals")
            print("4. ❌ Cancelled Rentals")
            
            status_map = {
                '1': 'pending',
                '2': 'active',
                '3': 'completed',
                '4': 'cancelled'
            }
            
            status_choice = get_input("\nChoose status (1-4): ")
            if status_choice in status_map:
                status = status_map[status_choice]
                rentals = rental_sys.get_rental_history_by_customer(
                    status=status
                )
                if rentals:
                    print_detailed_rental_history(rentals)
                else:
                    print_info(f"No {status} rentals found")
            else:
                print_error("Invalid status choice")
        
        if choice != '6':
            get_input("\nPress Enter to continue...")


def handle_booking_requests(rental_sys, auth, user_data):
    """Handle pending booking requests"""
    # Get all rentals
    rentals = rental_sys.get_all_rentals(user_data['user_id'])  # Pass admin's user_id
    if not rentals:
        print_info("No rentals in the system")
        return
        
    # Filter for pending rentals only
    pending_rentals = [r for r in rentals if r['status'] == 'pending']
    
    if not pending_rentals:
        print_info("No pending booking requests")
        return
    
    print("\n=== 📋 PENDING BOOKING REQUESTS ===")
    print(f"Total Pending Requests: {len(pending_rentals)}")
    print("-" * 50)
    
    for rental in pending_rentals:
        # Get customer details
        customer = auth.get_customer_details(rental['user_id'])
        if not customer:
            continue
            
        # Format customer name
        name = f"{customer.get('first_name', '')} {customer.get('last_name', '')}"
        
        # Format rental details
        print(f"\n🔖 Request #{rental['rental_id']}:")
        print(f"   👤 Customer: {name}")
        print(f"   📞 Phone:    {customer.get('phone_number', 'Not provided')}")
        print(f"   🚗 Car:      {rental['car']}")
        print(f"   📅 Period:   {rental['start_date'][:10]} to {rental['end_date'][:10]}")
        print(f"   💰 Amount:   ${rental['total_cost']:.2f}")
        print(f"   ⏳ Status:   {format_rental_status(rental['status'])}")
        print("-" * 40)
    
    while True:
        print("\nOptions:")
        print("1. ✅ Approve Request")
        print("2. ⛔ Reject Request")
        print("3. ↩️  Back")
        
        choice = get_input("\nEnter choice (1-3): ")
        
        if choice == '3':  # Back
            break
            
        if choice in ['1', '2']:
            try:
                req_id = int(get_input("\nEnter request number (0 to cancel): "))
                if req_id == 0:
                    continue
                    
                # Verify request exists
                request = next(
                    (r for r in pending_rentals if r['rental_id'] == req_id),
                    None
                )
                
                if not request:
                    print_error("Invalid request number")
                    continue
                
                # Handle approval/rejection
                status = 'approved' if choice == '1' else 'rejected'
                result = rental_sys.update_rental_status(
                    req_id, 
                    status,
                    admin_id=user_data['user_id']  # Pass the admin's user_id
                )
                
                if result[0]:  # Success
                    msg = "Request approved!" if status == 'approved' else "Request rejected!"
                    print_success(msg)
                    break
                else:
                    print_error(result[1])
                    
            except ValueError:
                print_error("Please enter a valid request number")
        
        get_input("\nPress Enter to continue...")


def handle_manage_bookings(auth, rental_sys, user_data):
    """Handle booking management for customers"""
    while True:
        # Get user's rentals
        rentals = rental_sys.get_user_rentals(user_data['user_id'])
        
        # Filter pending rentals
        pending_rentals = [
            r for r in rentals if r['status'] == 'pending'
        ]
        
        if not pending_rentals:
            print_info("No pending bookings found")
            return
        
        print("\n=== 📝 MANAGE BOOKINGS ===")
        print("Pending Bookings:")
        print("-" * 50)
        
        for rental in pending_rentals:
            # Format rental details
            car = rental['car']
            start = rental['start_date'][:10]
            end = rental['end_date'][:10]
            days = int(rental['rental_days'])
            amount = f"${rental['total_cost']:.2f}"
            status = format_rental_status(rental['status'])  # Using the detailed status format
            
            print(f"\n🔖 Booking #{rental['rental_id']}:")
            print(f"   • Car:      {car}")
            print(f"   • Period:   {start} to {end} ({days} days)")
            print(f"   • Amount:   {amount}")
            print(f"   • Status:   {status}")
        
        print("\nOptions:")
        print("1. ❌ Cancel Booking")
        print("2. ↩️  Back")
        
        choice = get_input("\nEnter choice (1-2): ")
        
        if choice == '2':  # Back
            break
            
        elif choice == '1':  # Cancel Booking
            prompt = "\nEnter booking number to cancel (0 to cancel): "
            booking_id = get_input(prompt)
            if not booking_id or booking_id == '0':
                continue
                
            try:
                booking_id = int(booking_id)
                # Verify booking exists and belongs to user
                booking = next(
                    (r for r in pending_rentals 
                     if r['rental_id'] == booking_id),
                    None
                )
                
                if not booking:
                    print_error("Invalid booking number")
                    continue
                
                # Confirm cancellation
                confirm = get_input(
                    "Are you sure you want to cancel? (y/n): "
                )
                if confirm.lower() == 'y':
                    success, msg = rental_sys.cancel_rental(
                        booking_id,
                        user_data['user_id']
                    )
                    if success:
                        print_success(msg)
                    else:
                        print_error(msg)
                
            except ValueError:
                print_error("Please enter a valid booking number")
        
        get_input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()