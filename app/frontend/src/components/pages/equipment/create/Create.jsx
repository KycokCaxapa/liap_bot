import React, { useState } from 'react'

import { createEquipment } from '../../../../services/api'

import styles from './create.module.css'

export default function Create() {
	const [modalWindow, setModalWindow] = useState(false)
	const [formData, setFormData] = useState({
		thing: null,
		amount: null,
		auditorium: null,
	})

	const handleSubmit = async () => {
		if (!formData.thing || !formData.amount || !formData.auditorium) {
			alert('Все поля должны быть заполнены.')
			return
		}

		const data = {
			thing: formData.thing,
			amount: formData.amount,
			auditorium: formData.auditorium,
		}

		try {
			await createEquipment(data)
			setModalWindow(false)
		} catch (error) {
			alert('Ошибка при создании оборудования.')
		}
	}

	return (
		<section>
			<button
				className={styles.addEquipment}
				onClick={() => setModalWindow(true)}
			>
				Добавить оборудование
			</button>
			{modalWindow && (
				<section className={styles.modal}>
					<h1 className={styles.title}>Создание оборудования</h1>
					<label>
						Оборудование:
						<input
							type='text'
							value={formData.thing}
							onChange={e =>
								setFormData(prev => ({ ...prev, thing: e.target.value }))
							}
						/>
					</label>
					<label>
						Количество:
						<input
							type='number'
							value={formData.amount}
							onChange={e =>
								setFormData(prev => ({ ...prev, amount: e.target.value }))
							}
						/>
					</label>
					<label>
						Номер аудитории:
						<input
							type='text'
							value={formData.auditorium}
							onChange={e =>
								setFormData(prev => ({
									...prev,
									auditorium: e.target.value,
								}))
							}
						/>
					</label>
					<button className={styles.createEquipment} onClick={handleSubmit}>
						Создать оборудование
					</button>
					<button
						className={styles.closeModal}
						onClick={() => setModalWindow(false)}
					>
						Закрыть окно
					</button>
				</section>
			)}
		</section>
	)
}
