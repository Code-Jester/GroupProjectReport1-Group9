class WorkerProfileRequired(Exception):
    """Raised when the authenticated user does not have a Worker profile."""
    pass


class JobClosed(Exception):
    """Raised when applying for a job opportunity that is not open."""
    pass


class DuplicateApplication(Exception):
    """Raised when a worker has already applied for the same job."""
    pass