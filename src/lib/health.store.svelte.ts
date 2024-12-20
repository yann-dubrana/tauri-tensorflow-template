import {getServerHealth} from "$lib/client"; // Assuming this is your generated API client

const MAX_RETRIES = 10;
const INITIAL_RETRY_MS = 1000;

class ServerHealthState {
    isReady: boolean = $state(false);
    status: string = $state('unknown');
    error: string | null = $state(null);
    retryCount: number = $state(0);
    retryTimeout: number = $state(INITIAL_RETRY_MS);
    timeoutId: any | null = $state(null);

    async check() {
        try {
            let query = await getServerHealth();
            if (!query.data || query.error) {
                this.error = query.error as string;
                this.isReady = false
                this.status = 'unhealthy';
            } else {
                this.status = query.data?.status;
                this.isReady = true;
                this.error = null;
            }
            if (this.timeoutId) {
                clearInterval(this.timeoutId);
            }
        } catch (err) {
            if (this.retryCount >= MAX_RETRIES) {
                this.error = 'Max retries reached. Backend service may be down.'
                this.isReady = false
                return
            }
            const newTimeout = this.retryTimeout * 2;
            if (this.timeoutId) {
                clearInterval(this.timeoutId);
            }
            this.timeoutId = setInterval(this.check, newTimeout);
        }
    }
}


export const serverHealthStore = new ServerHealthState();