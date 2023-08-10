# Entry Exit System with ID Card Scanning

This Python program is designed to manage entry and exit to a room, event, or conference using ID card scanning. The program retrieves data from scanned ID cards, keeps track of the number of people inside the room, and ensures controlled entry for the next participant while maintaining the maximum occupancy limit.

## Features

- Scan ID Cards: The program can scan ID cards of students or employees to retrieve their information.

- Occupancy Tracking: The program keeps track of the number of people currently inside the room or event.

- Controlled Entry: The program controls the entry of the next participant based on the maximum occupancy limit. It ensures that the maximum count inside the room is not exceeded.

## Requirements

- Python 3.x: Make sure you have Python 3.x installed on your system.

- Libraries: The program uses certain libraries that need to be installed. You can install them using the following command:

  ```bash
  pip install requirements.txt
  ```

## Usage

1. Run the program: Open a terminal or command prompt and navigate to the directory containing the program files. Run the program using the following command:

   ```bash
   python main.py
   ```

2. Scanning ID Cards: The program will prompt you to scan an ID card using the scanning device connected to your system.

3. Occupancy Management: The program will display the current occupancy and the maximum occupancy limit. It will then decide whether to allow entry to the next participant or wait until the occupancy decreases.

4. Exiting the Room: When a participant leaves the room, press the designated exit button in the program. The program will update the occupancy accordingly.

5. Closing the Program: To exit the program, press the designated exit key or follow the on-screen instructions.

## Configuration

- Maximum Occupancy: You can configure the maximum occupancy limit by modifying the `MAX_OCCUPANCY` variable in the program.

- Scanning Device: The program assumes that a scanning device (e.g., qr code scanner) is connected to the system. Make sure to configure the device settings if necessary.

## Future Enhancements

This program serves as a basic implementation of an entry-exit system. You can enhance it by adding features such as:

- **Database Integration:** Store scanned ID card data in a database for future reference.

- **User Interface:** Develop a graphical user interface (GUI) for a more user-friendly experience.

- **Notifications:** Send notifications when the maximum occupancy is reached or when it's safe to enter.

- **Access Control:** Integrate with access control systems to automate door opening and closing.

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to create a pull request.

## License

This program is released under the [MIT License](LICENSE).

---

Please ensure that you have read and understood the documentation before using the program. If you encounter any issues or have questions, contact me at [shashank21005@gmail.com](mailto:shashank21005@gmail.com).
