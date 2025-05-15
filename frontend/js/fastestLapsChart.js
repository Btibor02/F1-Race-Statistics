fetch('/api/races/fastest_laps') 
  .then(res => res.json())
  .then(data => {
    const ctx = document.getElementById('fastestLapsChart').getContext('2d');

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.drivers,
        datasets: [{
          label: 'Fastest Lap Time (seconds)',
          data: data.times,
          backgroundColor: data.drivers.map(() => randomColor())
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Fastest Lap Times per Driver'
          }
        },
        scales: {
          y: {
            beginAtZero: false,
            title: { display: true, text: 'Seconds' }
          },
          x: {
            title: { display: true, text: 'Driver' }
          }
        }
      }
    });
  });

function randomColor() {
  const r = Math.floor(Math.random() * 150);
  const g = Math.floor(Math.random() * 150);
  const b = Math.floor(Math.random() * 150);
  return `rgb(${r},${g},${b})`;
}
