import { Link } from 'react-router-dom'

import styles from './footer.module.css'

export default function Footer() {
	return (
		<footer className={styles.footer}>
			<div className={styles.auditoriums}>
				<Link to='/auditoriums'>
					<a className={styles.button}>
						<img
							src='https://cdn-icons-png.flaticon.com/128/4700/4700426.png'
							alt='logo'
							className={styles.buttonImg}
						/>
						<span className={styles.buttonText}>Аудитории</span>
					</a>
				</Link>
			</div>
			<div className={styles.equipment}>
				<Link to='/equipment'>
					<a className={styles.button}>
						<img
							src='https://static.thenounproject.com/png/252398-200.png'
							alt='logo'
							className={styles.buttonImg}
						/>
						<span className={styles.buttonText}>Оборудование</span>
					</a>
				</Link>
			</div>
		</footer>
	)
}
