fetch('/api/races/speed_trap')
  .then(res => res.json())
  .then(data => {

    const ctx = document.getElementById('speedTrapChart').getContext('2d');

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.drivers,
        datasets: [{
          label: 'Speed Trap (km/h)',
          data: data.speeds,
          backgroundColor: data.drivers.map(() => randomColor())
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Speed Trap Results'
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            title: { display: true, text: 'Speed (km/h)' }
          },
          y: {
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
