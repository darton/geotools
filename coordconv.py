from math import floor

def convert_coordinates(coord_string):
    try:
        # Rozdzielenie współrzędnych na szerokość i długość geograficzną
        lat_str, lon_str = coord_string.split(", ")
        lat = float(lat_str)
        lon = float(lon_str)

        # Przetwarzanie szerokości geograficznej
        lat_deg = floor(lat)
        lat_min = (lat - lat_deg) * 60
        lat_formatted = f"{lat_deg:03}{lat_min:05.3f}N"

        # Przetwarzanie długości geograficznej
        lon_deg = floor(lon)
        lon_min = (lon - lon_deg) * 60
        lon_formatted = f"{lon_deg:03}{lon_min:06.3f}E"

        return f"{lat_formatted}, {lon_formatted}"
    
    except ValueError:
        return "Błąd: Niepoprawny format współrzędnych. Użyj formatu '49.76146, 20.66106'."

if __name__ == "__main__":
    coord_input = input("Podaj współrzędne (format: 49.76146, 20.66106): ")
    
    converted = convert_coordinates(coord_input)
    print(f"Skonwertowane współrzędne: {converted}")