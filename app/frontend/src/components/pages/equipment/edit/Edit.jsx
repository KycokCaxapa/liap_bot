import { useState } from 'react'

import { updateEquipment, deleteEquipment } from '../../../../services/api'

import styles from './edit.module.css'

export default function Edit({ id, thing, amount, auditorium }) {
	const [modalWindow, setModalWindow] = useState(false)
	const [formData, setFormData] = useState({
		id: id,
		thing: thing,
		amount: amount,
		auditorium: auditorium,
	})

	const handleSubmit = async () => {
		const data = {
			id: id,
			thing: formData.thing,
			amount: formData.amount,
			auditorium: formData.auditorium,
		}

		try {
			await updateEquipment(data)
			setModalWindow(false)
		} catch (error) {
			alert('Ошибка при обновлении оборудования.')
		}
	}

	const handleDelete = async () => {
		try {
			const param = new URLSearchParams()
			param.append('id', id)

			await deleteEquipment(param)
			setModalWindow(false)
		} catch (error) {
			alert('Ошибка при удалении оборудования.')
		}
	}

	return (
		<section>
			<button onClick={() => setModalWindow(true)}>
				<img className={styles.editImg} src='/assets/edit.svg' />
			</button>
			{modalWindow && (
				<section className={styles.modal}>
					<h1 className={styles.title}>Редактирование оборудования</h1>
					<label>
						Оборудование:
						<input
							type='text'
							value={formData.thing}
							onChange={e =>
								setFormData(prev => ({
									...prev,
									thing: e.target.value,
								}))
							}
						/>
					</label>
					<label>
						Количество:
						<input
							type='number'
							value={formData.amount}
							onChange={e =>
								setFormData(prev => ({
									...prev,
									amount: e.target.value,
								}))
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
					<button className={styles.editEquipment} onClick={handleSubmit}>
						Обновить оборудование
					</button>
					<button className={styles.deleteEquipment} onClick={handleDelete}>
						Удалить оборудование
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
