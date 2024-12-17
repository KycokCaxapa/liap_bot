import React, { useState } from 'react'

import { createAuditorium } from '../../../../services/api'

import styles from './createAuditorium.module.css'

export default function Create() {
	const [modalWindow, setModalWindow] = useState(false)
	const [formData, setFormData] = useState({
		number: null,
		members: null,
		projector: false,
	})

	const handleSubmit = async () => {
		if (!formData.number || !formData.members) {
			alert('Все поля должны быть заполнены.')
			return
		}

		const data = {
			number: formData.number,
			members: formData.members,
			projector: formData.projector,
			equipment: null,
		}

		try {
			await createAuditorium(data)
			setModalWindow(false)
		} catch (error) {
			alert('Ошибка при создании аудитории. Проверьте данные.')
		}
	}

	return (
		<section>
			<button
				className={styles.addAuditorium}
				onClick={() => setModalWindow(true)}
			>
				Добавить аудиторию
			</button>
			{modalWindow && (
				<section className={styles.modal}>
					<h1 className={styles.title}>Создание аудитории</h1>
					<label>
						Номер аудитории:
						<input
							type='text'
							value={formData.number}
							onChange={e =>
								setFormData(prev => ({ ...prev, number: e.target.value }))
							}
						/>
					</label>
					<label>
						Кол-во студентов:
						<input
							type='number'
							value={formData.members}
							onChange={e =>
								setFormData(prev => ({ ...prev, members: e.target.value }))
							}
						/>
					</label>
					<label>
						Проектор:
						<input
							type='checkbox'
							value={formData.projector}
							onChange={e =>
								setFormData(prev => ({
									...prev,
									projector: e.target.checked,
								}))
							}
						/>
					</label>
					<button className={styles.createAuditorium} onClick={handleSubmit}>
						Создать аудиторию
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
