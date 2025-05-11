import React, { useEffect, useState } from 'react';
import API from '../api';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Dashboard() {
  const [userData, setUserData] = useState(null);
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    API.get('/api/profile') // This endpoint should return the logged-in user's data
      .then(res => {
        const user = res.data;
        setUserData(user);

        // Dummy data until backend sends aggregated stats
        const data = [
          { name: 'Driver 1', value: user.fav_driver_1 === 'dri1' ? 1 : 0 },
          { name: 'Driver 2', value: user.fav_driver_1 === 'dri2' ? 1 : 0 },
          { name: 'Driver 3', value: user.fav_driver_1 === 'dri3' ? 1 : 0 }
        ];
        setChartData(data);
      })
      .catch(err => console.error(err));
  }, []);

  if (!userData) return <p>Loading...</p>;

  return (
    <div className="p-4">
      <h2>Welcome, {userData.username}</h2>
      <p>Email: {userData.email}</p>

      <h3 className="mt-5">Favorite Driver Distribution</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" fill="#8884d8" name="Selections" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Dashboard;
