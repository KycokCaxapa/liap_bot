import { useEffect, useState } from 'react'

import EquipmentFilters from './equipmentFilters/EquipmentFilters'
import CreateEquipment from './createEquipment/createEquipment'
import EditEquipment from './editEquipment/EditEquipment'
import { fetchEquipment } from '../../../services/api'

import styles from './equipment.module.css'

export default function Equipment({ userRole }) {
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
				<CreateEquipment userRole={userRole} />
				<EquipmentFilters
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
						<EditEquipment
							userRole={userRole}
							id={equipment.id}
							thing={equipment.thing}
							amount={equipment.amount}
							auditorium={equipment.auditorium}
						/>
					</li>
				))}
			</ul>
		</main>
	)
}
