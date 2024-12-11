import { useState } from 'react'

import { updateAuditorium, deleteAuditorium } from '../../../../services/api'

import styles from './editAuditorium.module.css'

export default function EditAuditorium({
	userRole,
	id,
	number,
	members,
	projector,
}) {
	const [modalWindow, setModalWindow] = useState(false)
	const [formData, setFormData] = useState({
		id: id,
		number: number,
		members: members,
		projector: projector,
	})

	const handleSubmit = async () => {
		const data = {
			id: id,
			number: formData.number,
			members: formData.members,
			projector: formData.projector,
		}

		try {
			await updateAuditorium(data)
			setModalWindow(false)
		} catch (error) {
			alert('Ошибка при обновлении аудитории.')
		}
	}

	const handleDelete = async () => {
		try {
			const param = new URLSearchParams()
			param.append('id', id)

			await deleteAuditorium(param)
			setModalWindow(false)
		} catch (error) {
			alert('Ошибка при удалении аудитории.')
		}
	}

	if (userRole === 'admin' || userRole === 'teacher') {
		return (
			<section>
				<button onClick={() => setModalWindow(true)}>
					<img className={styles.editImg} src='/assets/edit.png' />
				</button>
				{modalWindow && (
					<section className={styles.modal}>
						<h1 className={styles.title}>Редактирование аудитории</h1>
						<label>
							Номер аудитории:
							<input
								type='text'
								value={formData.number}
								onChange={e =>
									setFormData(prev => ({
										...prev,
										number: e.target.value,
									}))
								}
							/>
						</label>
						<label>
							Кол-во студентов:
							<input
								type='number'
								value={formData.members}
								onChange={e =>
									setFormData(prev => ({
										...prev,
										members: e.target.value,
									}))
								}
							/>
						</label>
						<label>
							Проектор:
							<input
								type='checkbox'
								checked={formData.projector}
								onChange={e =>
									setFormData(prev => ({
										...prev,
										projector: e.target.checked,
									}))
								}
							/>
						</label>
						<button className={styles.editAuditorium} onClick={handleSubmit}>
							Обновить аудиторию
						</button>
						<button className={styles.deleteAuditorium} onClick={handleDelete}>
							Удалить аудиторию
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
}
