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

export const createAuditorium = async data => {
	try {
		await API.post('/auditorium/create', data)
	} catch (error) {
		console.error(`Ошибка при отправке аудитории: ${error}`)
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

export const updateAuditorium = async data => {
	try {
		await API.put('/auditorium/update', data)
	} catch (error) {
		console.error(`Ошибка при обновлении аудитории: ${error}`)
		throw error
	}
}

export const deleteAuditorium = async param => {
	try {
		await API.delete('/auditorium/delete', {
			params: param,
		})
	} catch (error) {
		console.error(`Ошибка при удалении аудитории: ${error}`)
		throw error
	}
}

export const createEquipment = async data => {
	try {
		await API.post('/equipment/create', data)
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

export const updateEquipment = async data => {
	try {
		await API.put('/equipment/update', data)
	} catch (error) {
		console.error(`Ошибка при обновлении оборудования: ${error}`)
		throw error
	}
}

export const deleteEquipment = async param => {
	try {
		await API.delete('/equipment/delete', {
			params: param,
		})
	} catch (error) {
		console.error(`Ошибка при удалении оборудования: ${error}`)
		throw error
	}
}