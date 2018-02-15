import sqlite3

db_url = 'mileage.db'   # Assumes the table miles have already been created.

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles

    If the vehicle is None or new_miles is not a positive number, raise Error
    '''

    # Make vehicle to uppercase
    vehicle = vehicle.upper()

    if not vehicle:
        raise Exception('Provide a vehicle name')
    if isinstance(new_miles, float) or new_miles < 0:
        raise Exception('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()



def search_vehicle_mileage(vehicle):
    # Make vehicle to uppercase
    vehicle = vehicle.upper()

    if not vehicle:
        raise Exception('Provide a vehicle name')


    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    mileageData = cursor.execute('SELECT total_miles FROM MILES WHERE vehicle = ?', (str(vehicle),) ).fetchall()

    mileage = -1
    for row in mileageData:
        mileage = row[0]

    if mileage >= 0:
        return mileage
    else:
        return None


def main():
    while True:
        vehicle = input('Enter vehicle name or enter \'search\' to search for a car (Press enter to quit): ')
        if not vehicle:
            break
        elif vehicle.upper() == 'SEARCH':
            vehicle_search = input('Enter vehicle name to search: ')
            mileage = search_vehicle_mileage(vehicle_search)
            if mileage is None:
                print('{} does not exist in the database'.format(vehicle_search))
            else:
                print('Current mileage for {} is {} miles'.format(vehicle_search, mileage))

        else:
            miles = float(input('Enter new miles for %s: ' % vehicle)) ## TODO input validation

            add_miles(vehicle, miles)


if __name__ == '__main__':
    main()
