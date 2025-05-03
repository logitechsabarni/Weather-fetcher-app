const apiKey = d115f23a624b085d038b53324cc67d2f; // Replace with your OpenWeatherMap API key

function getWeather() {
  const city = document.getElementById("cityInput").value.trim();
  const resultDiv = document.getElementById("weatherResult");

  if (!city) {
    resultDiv.innerHTML = "❗ Please enter a city name.";
    return;
  }

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      if (data.cod !== 200) {
        resultDiv.innerHTML = `❌ Error: ${data.message}`;
        return;
      }

      const weather = data.weather[0].description;
      const temp = data.main.temp;
      const humidity = data.main.humidity;
      const wind = data.wind.speed;

      resultDiv.innerHTML = `
        <h3>Weather in ${city.charAt(0).toUpperCase() + city.slice(1)}</h3>
        <p>🌡️ Temperature: ${temp}°C</p>
        <p>☁️ Description: ${weather}</p>
        <p>💧 Humidity: ${humidity}%</p>
        <p>🌬️ Wind Speed: ${wind} m/s</p>
      `;
    })
    .catch(error => {
      resultDiv.innerHTML = "⚠️ Network error. Please try again later.";
      console.error(error);
    });
}
