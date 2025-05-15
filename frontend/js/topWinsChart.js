import { fetchJSON } from './utilities.js';

(async () => {
  const data = await fetchJSON('/api/standings/2024');
  const ctx = document.getElementById('topWinsChart').getContext('2d');
  new Chart(ctx, {
    type: 'horizontalBar',
    data,
    options: {
      responsive: true,
      plugins: { title: { display: true, text: 'Top Wins by Drivers' } }
    }
  });
})();