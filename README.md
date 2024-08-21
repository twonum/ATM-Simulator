## ATM Simulator with GUI and Database Integration

### 🚀 **Project Overview**

This project is a comprehensive ATM simulator application built with Python, Tkinter for the graphical user interface, and PyODBC for database connectivity. It provides a simulated ATM experience with functionalities such as user sign-up, sign-in, deposit, withdrawal, password reset, and account deletion. The application interacts with a SQL Server database to manage user data and transactions.

### 🔧 **Features**

- **User Authentication**:
  - **Sign-Up**: Create a new account with a username and password.
  - **Sign-In**: Log in to an existing account.
  - **Password Reset**: Update the password for an existing account.
  - **Account Deletion**: Permanently delete a user account.

- **Account Management**:
  - **Deposit**: Add funds to the user’s account balance.
  - **Withdraw**: Withdraw funds from the user’s account balance.
  - **Balance Display**: View the current balance of the account.

- **Database Integration**:
  - **SQL Server Database**: Store user credentials and balance information.
  - **CRUD Operations**: Perform create, read, update, and delete operations using SQL queries executed via PyODBC.

- **User Interface**:
  - **Sign-Up and Sign-In Forms**: Simple and intuitive forms for user interaction.
  - **Main ATM Screen**: Displays balance and allows deposit and withdrawal operations.
  - **Responsive Design**: Adjustments and feedback for user interactions.

### 💡 **Skills Demonstrated**

- **Python Programming**: Utilized core programming concepts, functions, and flow control to develop the application.
- **Tkinter**: Designed and managed the GUI for a smooth user experience.
- **Database Management (SQL Server)**: Implemented SQL queries for managing user data.
- **PyODBC**: Established a connection to SQL Server and executed SQL queries.
- **Error Handling**: Incorporated error handling and user feedback through message boxes.
- **User Authentication**: Developed secure sign-up, sign-in, and password reset functionalities.
- **UI/UX Design**: Created a visually appealing and user-friendly interface with consistent design elements.

### 💻 **Installation and Usage**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ATM-Simulator.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd ATM-Simulator
   ```

3. **Install Required Libraries**:
   ```bash
   pip install pyodbc
   ```

4. **Database Setup**:
   - Ensure you have SQL Server installed and configured.
   - Create a database named `ATM` and a table `Users` with the necessary columns (`Username`, `Password`, `Balance`).

5. **Run the Application**:
   ```bash
   python atm_simulator.py
   ```

### 📸 **Screenshots**

(Include screenshots of the application interface here)

### 📝 **Future Enhancements**

- **Enhanced Security**: Implement password hashing and additional security measures.
- **Feature Expansion**: Add more features like transaction history and user profiles.
- **Cross-Platform Support**: Adapt the application for different operating systems.

### 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
