import { useEffect, useState } from 'react'

import styles from './filters.module.css'

export default function Filters({
	applyFilters,
	initThingFilter = '',
	initMinAmountFilter = '',
}) {
	const [thingFilter, setThingFilter] = useState(initThingFilter)
	const [minAmountFilter, setMinAmountFilter] = useState(initMinAmountFilter)

	useEffect(() => {
		setThingFilter(initThingFilter)
		setMinAmountFilter(initMinAmountFilter)
	}, [initThingFilter, initMinAmountFilter])

	const handleApplyFilters = () => {
		applyFilters({
			thingFilter: thingFilter,
			minAmountFilter: minAmountFilter,
		})
	}

	return (
		<details>
			<summary>Фильтры</summary>
			<div className={styles.filters}>
				<div className={styles.thingFilter}>
					<label className={styles.thingLabel} htmlFor='thingFilter'>
						Оборудование:
					</label>
					<input
						id='thingFilter'
						className={styles.thingFilterField}
						type='text'
						placeholder='Название оборудования'
						value={thingFilter}
						onChange={e => setThingFilter(e.target.value)}
					/>
				</div>
				<div className={styles.minAmountFilter}>
					<label
						className={styles.minAmountFilterLabel}
						htmlFor='minAmountFilter'
					>
						Мин. количество:
					</label>
					<input
						id='minAmountFilter'
						className={styles.minAmountFilterField}
						type='number'
						placeholder='1'
						value={minAmountFilter}
						onChange={e => setMinAmountFilter(e.target.value)}
					/>
				</div>
				<button className={styles.submitFilters} onClick={handleApplyFilters}>
					Применить фильтры
				</button>
			</div>
		</details>
	)
}
