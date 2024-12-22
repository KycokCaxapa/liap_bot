import { useState } from 'react'

import { bookAuditorium } from '../../../../services/api'

import styles from './book.module.css'

export default function Book({ userID, auditoriumID, initIsBooked, bookedBy }) {
	const [isBooked, setIsBooked] = useState(initIsBooked)

	const handleBook = async () => {
		const param = new URLSearchParams()
		param.append('tg_id', userID)

		const data = {
			id: auditoriumID,
			is_booked: !isBooked,
		}

		try {
			await bookAuditorium(data, param)
			setIsBooked(!isBooked)
		} catch (error) {
			alert('Ошибка при бронировании аудитории.')
		}
	}

	return (
		<section className={styles.book}>
			{bookedBy && bookedBy !== userID && (
				<a
					className={styles.user}
					href={`tg://openmessage?user_id=${bookedBy}`}
					target='_blank'
				>
					Написать пользователю
				</a>
			)}
			{(!isBooked || (isBooked && bookedBy === userID)) && (
				<label className={styles.bookField}>
					Забронировать аудиторию
					<input
						className={styles.bookCheckbox}
						type='checkbox'
						checked={isBooked}
						onClick={handleBook}
					/>
				</label>
			)}
		</section>
	)
}
