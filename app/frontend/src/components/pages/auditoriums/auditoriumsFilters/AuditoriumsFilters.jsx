import { useEffect, useState } from 'react'
import { Slider } from '@mui/material'

import styles from './AuditoriumsFilters.module.css'

export default function AuditoriumsFilters({
	applyFilters,
	initNumberFilter = '',
	initMinMembersFilter = '',
	initMaxMembersFilter = '',
	initProjectorFilter = false,
}) {
	const [numberFilter, setNumberFilter] = useState(initNumberFilter)
	const [membersRangeFilter, setMembersRangeFilter] = useState([
		Number(initMinMembersFilter) || 1,
		Number(initMaxMembersFilter) || 200,
	])
	const [projectorFilter, setProjectorFilter] = useState(initProjectorFilter)

	useEffect(() => {
		setNumberFilter(initNumberFilter)
		setMembersRangeFilter([
			Number(initMinMembersFilter) || 1,
			Number(initMaxMembersFilter) || 200,
		])
		setProjectorFilter(initProjectorFilter)
	}, [
		initNumberFilter,
		initMinMembersFilter,
		initMaxMembersFilter,
		initProjectorFilter,
	])

	const handleApplyFilters = () => {
		const [minMembersNumber, maxMembersNumber] = membersRangeFilter.map(Number)

		applyFilters({
			numberFilter: numberFilter,
			minMembersFilter: minMembersNumber,
			maxMembersFilter: maxMembersNumber,
			projectorFilter: projectorFilter,
		})
	}

	const handleRangeChange = (event, newValue) => {
		if (!Array.isArray(newValue) || newValue.length !== 2) {
			console.error(`Invalid slider value: ${newValue}`)
		}
		setMembersRangeFilter(newValue)
	}

	return (
		<details>
			<summary>Фильтры</summary>
			<div className={styles.filters}>
				<div className={styles.numberFilter}>
					<label className={styles.numberLabel} htmlFor='numberFilter'>
						Номер аудитории:
					</label>
					<input
						id='numberFilter'
						className={styles.numberFilterField}
						type='number'
						placeholder='53-04'
						value={numberFilter}
						onChange={e => setNumberFilter(e.target.value)}
					/>
				</div>
				<div className={styles.membersFilter}>
					<label className={styles.membersLabel} htmlFor='membersFilter'>
						Количество мест:
					</label>
					<Slider
						value={membersRangeFilter}
						defaultValue={[0, 200]}
						onChange={handleRangeChange}
						valueLabelDisplay='auto'
						min={1}
						max={200}
						disableSwap
						sx={{ width: '150px' }}
					/>
				</div>
				<div className={styles.projectorFilter}>
					<label className={styles.projectorLabel} htmlFor='projectorFilter'>
						Проектор:
					</label>
					<input
						id='projectorFilter'
						className={styles.projectorFilterField}
						type='checkbox'
						checked={projectorFilter}
						onChange={e => setProjectorFilter(e.target.checked)}
					/>
				</div>
				<button className={styles.submitFilters} onClick={handleApplyFilters}>
					Применить фильтры
				</button>
			</div>
		</details>
	)
}
