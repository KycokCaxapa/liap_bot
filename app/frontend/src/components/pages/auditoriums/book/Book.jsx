import { useState } from 'react'

import { bookAuditorium } from '../../../../services/api'

import styles from './book.module.css'

export default function Book({
	userID,
	auditoriumID,
	initIsBooked,
	bookedBy,
}) {
	const [isBooked, setIsBooked] = useState(initIsBooked)

	const handleBook = async () => {
		const data = {
			id: auditoriumID,
			is_booked: !isBooked,
			tg_id: !isBooked ? userID : null,
		}

		try {
			await bookAuditorium(data)
			setIsBooked(!isBooked)
		} catch (error) {
			alert('Ошибка при бронировании аудитории.')
		}
	}

	return (
		<section className={styles.book}>
			<div className={styles.bookWrapper}>
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
					<input
						className={styles.bookField}
						type='checkbox'
						checked={isBooked}
						onClick={handleBook}
					/>
				)}
			</div>
		</section>
	)
}
