import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL
const API = axios.create({
	baseURL: API_URL,
})

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
