

import './App.css';
import { BrowserRouter as Router, Routes, Route, Link, NavLink } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';


function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 rounded">
          <div className="container-fluid">
            <Link className="navbar-brand fw-bold" to="/">
              <img src={process.env.PUBLIC_URL + '/octofitapp-small.png'} alt="Octofit Logo" className="me-2" style={{height: '40px', verticalAlign: 'middle'}} />
              Octofit Tracker
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item"><NavLink className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'} to="/activities">Activities</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'} to="/leaderboard">Leaderboard</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'} to="/teams">Teams</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'} to="/users">Users</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'} to="/workouts">Workouts</NavLink></li>
              </ul>
            </div>
          </div>
        </nav>
        <h1 className="mb-4 text-center fw-bold">Octofit Tracker</h1>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<div className="card p-4 text-center"><h2>Welcome to Octofit Tracker!</h2><p className="lead">Track your fitness, join teams, and compete on the leaderboard!</p></div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
