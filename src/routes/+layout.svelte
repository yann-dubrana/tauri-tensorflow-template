<script>
    import "../app.css";
    import {client} from "$lib/client";
    import {serverHealthStore} from "$lib/health.store.svelte";
    import Update from "$lib/components/Update.svelte";

    let {children} = $props();

    client.setConfig({baseUrl: 'http://127.0.0.1:63421/'});
    serverHealthStore.check()

</script>

{@render children()}
<Update/>