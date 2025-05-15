import { fetchJSON } from './utilities.js';

(async () => {
  const data = await fetchJSON('/api/standings/2024');
  const ctx = document.getElementById('driverStandingsChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data,
    options: {
      responsive: true,
      plugins: { title: { display: true, text: 'Driver Standings by Season' } }
    }
  });
})();