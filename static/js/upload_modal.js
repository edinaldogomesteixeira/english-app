const openModal =
    document.getElementById(
        'open-import-modal'
    )

const closeModal =
    document.getElementById(
        'close-import-modal'
    )

const cancelImport =
    document.getElementById(
        'cancel-import'
    )

const modal =
    document.getElementById(
        'import-modal'
    )

const dropArea =
    document.getElementById(
        'drop-area'
    )

const fileInput =
    document.getElementById(
        'file-input'
    )

const selectedFile =
    document.getElementById(
        'selected-file'
    )

const videoTitle =
    document.getElementById(
        'video-title'
    )

const videoDuration =
    document.getElementById(
        'video-duration'
    )

// OPEN MODAL

if (openModal) {

    openModal.addEventListener(
        'click',
        () => {

            modal.classList.remove(
                'hidden'
            )

            modal.classList.add(
                'flex'
            )

        }
    )

}

// CLOSE MODAL

function hideModal() {

    modal.classList.add(
        'hidden'
    )

    modal.classList.remove(
        'flex'
    )

}

if (closeModal) {

    closeModal.addEventListener(
        'click',
        hideModal
    )

}

if (cancelImport) {

    cancelImport.addEventListener(
        'click',
        hideModal
    )

}

if (modal) {

    modal.addEventListener(
        'click',
        (e) => {

            if (e.target === modal) {

                hideModal()

            }

        }
    )

}

// CLICK SELECT FILE

if (dropArea) {

    dropArea.addEventListener(
        'click',
        () => {

            fileInput.click()

        }
    )

}

// FILE SELECTED

if (fileInput) {

    fileInput.addEventListener(
        'change',
        () => {

            if (
                fileInput.files.length > 0
            ) {

                const file =
                    fileInput.files[0]

                selectedFile.innerText =
                    file.name

                // TITLE

                const filenameWithoutExtension =
                    file.name.replace(
                        /\.[^/.]+$/,
                        ""
                    )

                videoTitle.value =
                    filenameWithoutExtension

                // VIDEO DURATION

                const video =
                    document.createElement(
                        'video'
                    )

                video.preload =
                    'metadata'

                video.onloadedmetadata =
                    function () {

                        window.URL.revokeObjectURL(
                            video.src
                        )

                        const duration =
                            video.duration

                        const minutes =
                            Math.floor(
                                duration / 60
                            )

                        const seconds =
                            Math.floor(
                                duration % 60
                            )

                        videoDuration.value =
                            `${minutes}:${seconds
                                .toString()
                                .padStart(
                                    2,
                                    '0'
                                )}`

                    }

                video.src =
                    URL.createObjectURL(
                        file
                    )

            }

        }
    )

}

// DRAG OVER

if (dropArea) {

    dropArea.addEventListener(
        'dragover',
        (e) => {

            e.preventDefault()

            dropArea.classList.add(
                'bg-blue-100'
            )

        }
    )

}

// DRAG LEAVE

if (dropArea) {

    dropArea.addEventListener(
        'dragleave',
        () => {

            dropArea.classList.remove(
                'bg-blue-100'
            )

        }
    )

}

// DROP FILE

if (dropArea) {

    dropArea.addEventListener(
        'drop',
        (e) => {

            e.preventDefault()

            dropArea.classList.remove(
                'bg-blue-100'
            )

            fileInput.files =
                e.dataTransfer.files

            if (
                fileInput.files.length > 0
            ) {

                const file =
                    fileInput.files[0]

                selectedFile.innerText =
                    file.name

                // TITLE

                const filenameWithoutExtension =
                    file.name.replace(
                        /\.[^/.]+$/,
                        ""
                    )

                videoTitle.value =
                    filenameWithoutExtension

                // DURATION

                const video =
                    document.createElement(
                        'video'
                    )

                video.preload =
                    'metadata'

                video.onloadedmetadata =
                    function () {

                        window.URL.revokeObjectURL(
                            video.src
                        )

                        const duration =
                            video.duration

                        const minutes =
                            Math.floor(
                                duration / 60
                            )

                        const seconds =
                            Math.floor(
                                duration % 60
                            )

                        videoDuration.value =
                            `${minutes}:${seconds
                                .toString()
                                .padStart(
                                    2,
                                    '0'
                                )}`

                    }

                video.src =
                    URL.createObjectURL(
                        file
                    )

            }

        }
    )

}