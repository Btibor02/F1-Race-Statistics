import { fetchJSON } from './utilities.js';

(async () => {
  const data = await fetchJSON('/api/2024/drivers');
  const ctx = document.getElementById('nationalityPieChart').getContext('2d');
  new Chart(ctx, {
    type: 'pie',
    data,
    options: {
      responsive: true,
      plugins: { title: { display: true, text: 'Driver Nationalities Distribution' } }
    }
  });
})();
