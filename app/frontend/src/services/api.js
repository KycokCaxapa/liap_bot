import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL
const API = axios.create({
	baseURL: API_URL,
})

export const fetchUserRole = async tg_id => {
	try {
		const request = await API.get('/users/get_role', {
			params: { tg_id: tg_id },
		}).then(response => response.data)
		return request
	} catch (error) {
		console.error(`Ошибка при получении роли пользователя: ${error}`)
		throw error
	}
}

export const createAuditorium = async (data, param) => {
	try {
		await API.post('/auditorium/create', data, { params: param })
	} catch (error) {
		console.error(`Ошибка при создании аудитории: ${error}`)
		throw error
	}
}

export const fetchAuditoriums = async (params = null) => {
	try {
		const request = await API.get('/auditorium/get_by_filters', {
			params: params,
		}).then(response => response.data)
		return request
	} catch (error) {
		console.error(`Ошибка при получении аудиторий: ${error}`)
		throw error
	}
}

export const updateAuditorium = async (data, param) => {
	try {
		await API.put('/auditorium/update', data, { params: param })
	} catch (error) {
		console.error(`Ошибка при обновлении аудитории: ${error}`)
		throw error
	}
}

export const bookAuditorium = async (data, param) => {
	try {
		await API.put('/auditorium/book', data, { params: param })
	} catch (error) {
		console.error(`Ошибка при бронировании аудитории: ${error}`)
		throw error
	}
}

export const deleteAuditorium = async params => {
	try {
		await API.delete('/auditorium/delete', {
			params: params,
		})
	} catch (error) {
		console.error(`Ошибка при удалении аудитории: ${error}`)
		throw error
	}
}

export const createEquipment = async (data, param) => {
	try {
		await API.post('/equipment/create', data, { params: param })
	} catch (error) {
		console.error(`Ошибка при отправке оборудования: ${error}`)
		throw error
	}
}

export const fetchEquipment = async (params = null) => {
	try {
		const request = await API.get('/equipment/get_by_filters', {
			params: params,
		}).then(response => response.data)
		return request
	} catch (error) {
		console.error(`Ошибка при получении оборудования: ${error}`)
		throw error
	}
}

export const updateEquipment = async (data, param) => {
	try {
		await API.put('/equipment/update', data, { params: param })
	} catch (error) {
		console.error(`Ошибка при обновлении оборудования: ${error}`)
		throw error
	}
}

export const bookEquipment = async (data, param) => {
	try {
		await API.put('/equipment/book', data, { params: param })
	} catch (error) {
		console.error(`Ошибка при бронировании оборудования: ${error}`)
		throw error
	}
}

export const deleteEquipment = async params => {
	try {
		await API.delete('/equipment/delete', {
			params: params,
		})
	} catch (error) {
		console.error(`Ошибка при удалении оборудования: ${error}`)
		throw error
	}
}
