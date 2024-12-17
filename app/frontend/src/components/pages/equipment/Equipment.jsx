import { useEffect, useState } from 'react'

import { fetchEquipment } from '../../../services/api'
import Filters from './filters/Filters'
import Create from './create/Create'
import Edit from './edit/Edit'
import Book from './book/Book'

import styles from './equipment.module.css'

export default function Equipment({ userID, userRole }) {
	const [thingFilter, setThingFilter] = useState('')
	const [minAmountFilter, setMinAmountFilter] = useState()
	const [data, setData] = useState([])

	const applyFilters = ({ thingFilter, minAmountFilter }) => {
		setThingFilter(thingFilter)
		setMinAmountFilter(minAmountFilter)
	}

	useEffect(async () => {
		const params = new URLSearchParams()

		if (thingFilter) params.append('thing', thingFilter)
		if (minAmountFilter) params.append('min_amount', minAmountFilter)

		const response = await fetchEquipment(params)
		setData(response)
	}, [thingFilter, minAmountFilter])

	return (
		<main className={styles.main}>
			<section className={styles.buttons}>
				{(userRole === 'admin' || userRole === 'teacher') && (
					<Create />
				)}
				<Filters
					applyFilters={applyFilters}
					initThingFilter={thingFilter}
					initMinAmountFilter={minAmountFilter}
				/>
			</section>
			<ul className={styles.itemsList}>
				{data?.map((equipment, index) => (
					<li className={styles.item} key={index}>
						<span>
							Оборудование: {equipment.thing} * {equipment.amount}
						</span>
						<span>Аудитория: {equipment.auditorium}</span>
						{(userRole === 'admin' || userRole === 'teacher') && (
							<Edit
								id={equipment.id}
								thing={equipment.thing}
								amount={equipment.amount}
								auditorium={equipment.auditorium}
							/>
						)}
						{(userRole === 'admin' || userRole === 'student') && (
							<Book
								userID={userID}
								equipmentID={equipment.id}
								initAmount={equipment.amount}
								initIsBooked={equipment.booked_by}
							/>
						)}
					</li>
				))}
			</ul>
		</main>
	)
}
