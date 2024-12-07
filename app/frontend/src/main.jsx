import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { createRoot } from 'react-dom/client'
import { StrictMode } from 'react'

import Auditoriums from './components/pages/auditoriums/Auditoriums.jsx'
import Equipment from './components/pages/equipment/Equipment.jsx'
import Header from './components/header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'

import './styles.css'

createRoot(document.getElementById('root')).render(
	<StrictMode>
		<Router>
			<Header />
			<Routes>
				<Route path='/' element={<Auditoriums />} />
				<Route path='/auditoriums' element={<Auditoriums />} />
				<Route path='/equipment' element={<Equipment />} />
			</Routes>
			<Footer />
		</Router>
	</StrictMode>
)
