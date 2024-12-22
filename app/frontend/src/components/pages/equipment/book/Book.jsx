import { useEffect, useState } from 'react'

import { bookEquipment } from '../../../../services/api'

import styles from './book.module.css'

export default function Book({
	userID,
	equipmentID,
	initAmount,
	initIsBooked,
}) {
	const [amount, setAmount] = useState(initAmount)
	const [bookedBy, setBookedBy] = useState(initIsBooked)
	const isChecked = bookedBy === userID

	useEffect(() => {
		setAmount(initAmount)
		setBookedBy(initIsBooked)
	}, [initAmount, initIsBooked])

	const handleBook = async () => {
		const updatedAmount = isChecked ? amount + 1 : amount - 1
		const updatedBookedBy = isChecked ? null : userID

		const param = new URLSearchParams()
		param.append('tg_id', userID)

		const data = {
			id: equipmentID,
			amount: updatedAmount,
			booked_by: updatedBookedBy,
		}

		try {
			await bookEquipment(data, param)
			setAmount(updatedAmount)
			setBookedBy(updatedBookedBy)
		} catch (error) {
			alert(`Ошибка при бронировании оборудования.`)
		}
	}

	return (
		<section className={styles.book}>
			<label className={styles.bookField}>
				Забронировать оборудование
				<input
					className={styles.bookCheckbox}
					type='checkbox'
					checked={isChecked}
					onChange={handleBook}
					disable={!isChecked && amount < 0}
				/>
			</label>
		</section>
	)
}
