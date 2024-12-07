import { useEffect, useState } from 'react'

import AuditoriumsFilters from './auditoriumsFilters/AuditoriumsFilters'
import { fetchAuditoriums } from '../../../services/api'

import styles from './auditoriums.module.css'

export default function Auditoriums() {
	const [numberFilter, setNumberFilter] = useState('')
	const [minMembersFilter, setMinMembersFilter] = useState()
	const [maxMembersFilter, setMaxMembersFilter] = useState()
	const [projectorFilter, setProjectorFilter] = useState(false)
	const [data, setData] = useState([])

	const applyFilters = ({
		numberFilter,
		minMembersFilter,
		maxMembersFilter,
		projectorFilter,
	}) => {
		setNumberFilter(numberFilter)
		setMinMembersFilter(minMembersFilter)
		setMaxMembersFilter(maxMembersFilter)
		setProjectorFilter(projectorFilter)
	}

	const fetchData = async () => {
		const params = new URLSearchParams()

		if (numberFilter) params.append('number', numberFilter)
		if (minMembersFilter) params.append('min_members', minMembersFilter)
		if (maxMembersFilter) params.append('max_members', maxMembersFilter)
		if (projectorFilter) params.append('projector', projectorFilter)

		const response = await fetchAuditoriums(params)
		setData(response)
	}

	useEffect(() => {
		fetchData()
	}, [numberFilter, minMembersFilter, maxMembersFilter, projectorFilter])

	return (
		<main className={styles.main}>
			<AuditoriumsFilters
				applyFilters={applyFilters}
				initNumberFilter={numberFilter}
				initMinMembersFilter={minMembersFilter}
				initMaxMembersFilter={maxMembersFilter}
				initProjectorFilter={projectorFilter}
			/>
			<ul className={styles.itemsList}>
				{data?.map((auditorium, index) => (
					<li className={styles.item} key={index}>
						<span>Аудитория: {auditorium.number}</span>
						<span>Количество мест: {auditorium.members}</span>
						<span>Проектор: {auditorium.projector ? '✓' : '–'}</span>
						{auditorium.equipment.map(equipment => (
							<span>
								Оборудование: {equipment.thing} * {equipment.amount}
							</span>
						))}
					</li>
				))}
			</ul>
		</main>
	)
}
