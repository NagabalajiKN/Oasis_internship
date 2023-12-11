import requests
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

from datetime import datetime
def format_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%H:%M:%S UTC')

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            console = Console()
            
            # Convert sunrise and sunset timestamps to human-readable format
            sunrise_time = format_timestamp(data['sys']['sunrise'])
            sunset_time = format_timestamp(data['sys']['sunset'])
            panels = [
                Panel(f"Location : [cyan][bold]{data['name']}[/bold][/cyan]", title="[b]Location[/b]"),
                Panel(f"Temperature : [cyan]{data['main']['temp']}°C[/cyan]", title="[b]Temperature[/b]"),
                Panel(f"Humidity : [cyan]{data['main']['humidity']}%[/cyan]", title="[b]Humidity[/b]"),
                Panel(f"Condition : [cyan]{data['weather'][0]['description']}[/cyan]", title="[b]Condition[/b]"),
                
                Panel(f"Wind Speed : [cyan]{data['wind']['speed']}m/s[/cyan]", title="[b]Wind Speed[/b]"),
                Panel(f"Pressure : [cyan]{data['main']['pressure']}Pa[/cyan]", title="[b]Pressure[/b]"),
                Panel(f"Visibility : [cyan]{data['visibility']}m[/cyan]", title="[b]Visibility[/b]"),
                Panel(f"Country : [cyan]{data['sys']['country']}[/cyan]", title="[b]Country[/b]"),
                Panel(f"Sunrise: [cyan]{sunrise_time}[/cyan]", title="[b]Sunrise[/b]"),
                Panel(f"Sunset: [cyan]{sunset_time}[/cyan]", title="[b]Sunset[/b]"),

                
            ]
            print("\n")
            console.print(Columns(panels, equal=True))
            print("\n")
            

        else:
            print(f"Error: {data['message']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

console = Console()
api_key = ""  # api key


print("                                    ░██████╗██╗░░██╗██╗░░░██╗  ░██████╗███████╗███████╗██████╗░")
print("                                    ██╔════╝██║░██╔╝╚██╗░██╔╝  ██╔════╝██╔════╝██╔════╝██╔══██╗")
print("                                    ╚█████╗░█████═╝░░╚████╔╝░  ╚█████╗░█████╗░░█████╗░░██████╔╝")
print("                                    ░╚═══██╗██╔═██╗░░░╚██╔╝░░  ░╚═══██╗██╔══╝░░██╔══╝░░██╔══██╗")
print("                                    ██████╔╝██║░╚██╗░░░██║░░░  ██████╔╝███████╗███████╗██║░░██║")
print("                                    ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝")



# Subtitle with increased size using Unicode characters
subtitle_panel = Panel(Text("☀️  Today's Forecast ☀️ \n",justify="center"), style="bold blue",width=128)

console.print(subtitle_panel)
# Print the title and subtitle

location = input("Enter city or ZIP code: ")

get_weather(api_key, location)
