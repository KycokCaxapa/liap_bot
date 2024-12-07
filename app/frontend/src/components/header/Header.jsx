import React from 'react'

import styles from './Header.module.css'

export default function Header() {
	return (
		<header className={styles.header}>
			<img
				src='https://src.guap.ru/logos/guap/guap-sign.svg'
				alt='logo'
				className={styles.logo}
			/>
			<h1 className={styles.title}>ГУАП бронирование</h1>
		</header>
	)
}
