import { useEffect, useState } from 'react'

import AuditoriumsFilters from './auditoriumsFilters/AuditoriumsFilters'
import CreateAuditorium from './createAuditorium/CreateAuditorium'
import EditAuditorium from './editAuditorium/EditAuditorium'
import { fetchAuditoriums } from '../../../services/api'

import styles from './auditoriums.module.css'

export default function Auditoriums({ userRole }) {
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

	useEffect(async () => {
		const params = new URLSearchParams()

		if (numberFilter) params.append('number', numberFilter)
		if (minMembersFilter) params.append('min_members', minMembersFilter)
		if (maxMembersFilter) params.append('max_members', maxMembersFilter)
		if (projectorFilter) params.append('projector', projectorFilter)

		const response = await fetchAuditoriums(params)
		setData(response)
	}, [numberFilter, minMembersFilter, maxMembersFilter, projectorFilter])

	return (
		<main className={styles.main}>
			<section className={styles.buttons}>
				<CreateAuditorium userRole={userRole} />
				<AuditoriumsFilters
					applyFilters={applyFilters}
					initNumberFilter={numberFilter}
					initMinMembersFilter={minMembersFilter}
					initMaxMembersFilter={maxMembersFilter}
					initProjectorFilter={projectorFilter}
				/>
			</section>
			<ul className={styles.itemsList}>
				{data?.map(auditorium => (
					<li className={styles.item} key={auditorium.id}>
						<span>Аудитория: {auditorium.number}</span>
						<span>Количество мест: {auditorium.members}</span>
						<span>Проектор: {auditorium.projector ? '✓' : '–'}</span>
						<span>
							Оборудование:
							{auditorium.equipment.length > 0
								? auditorium.equipment
										.map(
											equipment => ` ${equipment.thing} * ${equipment.amount}`
										)
										.join(', ')
								: ' –'}
						</span>
						<EditAuditorium
							userRole={userRole}
							id={auditorium.id}
							number={auditorium.number}
							members={auditorium.members}
							projector={auditorium.projector}
						/>
					</li>
				))}
			</ul>
		</main>
	)
}
