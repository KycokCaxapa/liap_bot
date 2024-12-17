from fastapi import HTTPException, status


NOT_FOUND_404 = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail='Auditorium not found.')
ALREADY_EXISTS_409 = HTTPException(status_code=status.HTTP_409_CONFLICT,
                               detail='The record already exists and must be unique.')
UNAVAILABLE_409 = HTTPException(status_code=status.HTTP_409_CONFLICT,
                               detail='The amount of equipment does not allow booking.')
