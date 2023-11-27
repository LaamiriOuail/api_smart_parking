import serial
import cv2
import pytesseract


import mysql.connector

def get_connection()->tuple:
    # Establish a connection
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database="parking"
    )
    # Create a cursor
    cursor = connection.cursor()
    return connection,cursor
def search_car_by_matricule(matricule):
    # Establish a connection to the database
    connection ,cursor = get_connection()
    try:
        # Execute the query to search for a car by matricule
        query = "SELECT id ,matricule ,is_in_parking ,model ,client_id  FROM car WHERE matricule = %s"
        cursor.execute(query, (matricule,))
        # Fetch the result
        result = cursor.fetchone()

        if result:
            return result
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
def search_abonement_by_car_id(car_id):
    # Establish a connection to the database
    connection ,cursor = get_connection()
    try:
        # Execute the query to search for a car by matricule
        query = "SELECT id ,sold  FROM abonement WHERE car_id = %s"
        cursor.execute(query, (car_id,))
        # Fetch the result
        result = cursor.fetchone()

        if result:
            return result
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
def change_sold_abonemt_by_id_car(car_id,ticket):
    # Establish a connection to the database
    connection ,cursor = get_connection()
    try:
        # Execute the query to search for a car by matricule
        query = "SELECT id ,sold  FROM abonement WHERE car_id = %s"
        cursor.execute(query, (car_id,))
        # Fetch the result
        result = cursor.fetchone()

        if result:
            return result
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
ticket=3.5

# import numpy as np

# ...

def main(serial_port: str):
    # Initialize the serial connection
    try:
        ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
        print(f"Serial connection established on port {serial_port}")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()
            matricule:str = pytesseract.image_to_string(frame)
            matricule = matricule.strip()

            try:
                existing_car = search_car_by_matricule(matricule)
            except Exception as e:
                existing_car = False
                print(f"Error searching for car: {e}")

            # ... (rest of your code remains unchanged)

            if existing_car:
                # ... (rest of your code remains unchanged)

                if is_in_parking:
                    print("o")  # Serial
                    ser.write(b'o')  # Sending 'o' to the serial port
                    cv2.putText(frame, "Car in parking - Open door before user enters", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    print("c")  # Serial
                    ser.write(b'c')  # Sending 'c' to the serial port
                else:
                    # ... (rest of your code remains unchanged)

                    if sold >= ticket:
                        print("O")  # Serial
                        ser.write(b'O')  # Sending 'O' to the serial port
                        cv2.putText(frame, "Car exists but is not in the parking. Open door after user exits", (10, 70),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    else:
                        print("s")  # Serial : sold insuffisant
                        ser.write(b's')  # Sending 's' to the serial port
                    cv2.putText(frame, "Car not in parking - Open door after user exits", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    print("c")  # Serial
                    ser.write(b'c')  # Sending 'c' to the serial port
            else:
                print("n")  # Serial
                ser.write(b'n')  # Sending 'n' to the serial port
                cv2.putText(frame, "Car not found - Not a client", (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 0, 255), 2)

            # ... (rest of your code remains unchanged)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Camera closed.")
        # Close the serial connection
        ser.close()

# ... (rest of your code remains unchanged)

if __name__ == "__main__":
    main("COM1")  # Change "COM1" to the correct serial port on your system
