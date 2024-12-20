<script>
    import "../app.css";
    import {client} from "$lib/client";
    import {onMount} from "svelte";
    import {serverHealthStore} from "$lib/health.store.svelte";
    import Update from "$lib/components/Update.svelte";

    let {data, children} = $props();

    client.setConfig({
        baseUrl: 'http://localhost:63421/'
    });

    onMount(async () => {
        await serverHealthStore.check()
    });

</script>

{@render children()}
<Update/>