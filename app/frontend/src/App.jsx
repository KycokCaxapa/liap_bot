import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'

import Auditoriums from './components/pages/auditoriums/Auditoriums.jsx'
import Equipment from './components/pages/equipment/Equipment.jsx'
import Header from './components/header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'
import { fetchUserRole } from './services/api.js'

import './styles.css'

export default function App() {
	const [userID, setUserID] = useState(null)
	const [userRole, setUserRole] = useState(null)

	useEffect(async () => {
		const tg = window.Telegram.WebApp
		tg.ready()
		const userID = tg.initDataUnsafe.user.id
		setUserID(userID)
		await fetchUserRole(userID).then(response => setUserRole(response))
	}, [])

	if (userRole)
		return (
			<Router>
				<Header />
				<Routes>
					<Route
						path='/'
						element={<Auditoriums userID={userID} userRole={userRole} />}
					/>
					<Route
						path='/auditoriums'
						element={<Auditoriums userID={userID} userRole={userRole} />}
					/>
					<Route
						path='/equipment'
						element={<Equipment userID={userID} userRole={userRole} />}
					/>
				</Routes>
				<Footer />
			</Router>
		)
}
