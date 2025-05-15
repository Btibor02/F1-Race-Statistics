fetch('/api/races/lap_times')
  .then(res => res.json())
  .then(data => {
    const ctx = document.getElementById('lapTimeChart').getContext('2d');

    const datasets = data.datasets.map(driverData => ({
      label: driverData.driver,
      data: driverData.data,
      fill: false,
      borderColor: randomColor(),
      tension: 0.1
    }));
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.labels,
        datasets: datasets
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Lap Times per Driver'
          }
        },
        scales: {
          y: {
            title: { display: true, text: 'Lap Time (seconds)' }
          },
          x: {
            title: { display: true, text: 'Lap Number' }
          }
        }
      }
    });
  });

//random colors for variety
function randomColor() {
  const r = Math.floor(Math.random() * 150);
  const g = Math.floor(Math.random() * 150);
  const b = Math.floor(Math.random() * 150);
  return `rgb(${r},${g},${b})`;
}
