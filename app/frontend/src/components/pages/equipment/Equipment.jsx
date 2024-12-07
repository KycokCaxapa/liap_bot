import { useEffect, useState } from 'react'

import EquipmentFilters from './equipmentFilters/EquipmentFilters'
import { fetchEquipment } from '../../../services/api'
import styles from './equipment.module.css'

export default function Equipment() {
	const [thingFilter, setThingFilter] = useState('')
	const [minAmountFilter, setMinAmountFilter] = useState()
	const [data, setData] = useState([])

	const applyFilters = ({ thingFilter, minAmountFilter }) => {
		setThingFilter(thingFilter)
		setMinAmountFilter(minAmountFilter)
	}

	const fetchData = async () => {
		const params = new URLSearchParams()

		if (thingFilter) params.append('thing', thingFilter)
		if (minAmountFilter) params.append('min_amount', minAmountFilter)

		const response = await fetchEquipment(params)
		setData(response)
	}

	useEffect(() => {
		fetchData()
	}, [thingFilter, minAmountFilter])

	return (
		<main className={styles.main}>
			<EquipmentFilters
				applyFilters={applyFilters}
				initThingFilter={thingFilter}
				initMinAmountFilter={minAmountFilter}
			/>
			<ul className={styles.itemsList}>
				{data?.map((equipment, index) => (
					<li className={styles.item} key={index}>
						<span>
							Оборудование: {equipment.thing} * {equipment.amount}
						</span>
						<span>Аудитория: {equipment.auditorium_id}</span>
					</li>
				))}
			</ul>
		</main>
	)
}
