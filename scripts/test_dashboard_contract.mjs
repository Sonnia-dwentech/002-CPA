import assert from "node:assert/strict";
import { isDashboard, validFilters } from "../frontend/lib/dashboard.ts";
const row = {id:"00000000-0000-0000-0000-00000000000b", owner_id:"00000000-0000-0000-0000-000000000001",kind:"idea",state:"draft"};
const valid = {status:"ok",total:1,records:[row],available_kinds:["idea"],data_kind:"synthetic_reference_records",metric:"visible_reference_count",business_metrics_status:"unavailable"};
assert.equal(isDashboard(valid),true);
for (const payload of [null, {}, {...valid,total:2}, {...valid,total:2,records:[row,row]}, {...valid,status:"empty"}, {...valid,status:"unavailable",total:0,records:[]}, {...valid,records:[{...row,kind:"secret"}]}, {...valid,records:[{...row,id:"invalid"}]}, {...valid,data_kind:"production"}, {...valid,available_kinds:[]}]) {
  assert.equal(isDashboard(payload), false);
}
assert.equal(isDashboard({...valid,status:"empty",total:0,records:[]}),true);
assert.equal(isDashboard({...valid,status:"unavailable",total:null,records:[]}),true);
for (const query of ["kind=idea&kind=dossier", "kind=secret", "state=bad", "owner_id=bad", "sort=id", "kind="]) assert.equal(validFilters(new URLSearchParams(query)),false);
assert.equal(validFilters(new URLSearchParams("kind=idea&state=draft&owner_id="+row.owner_id)),true);
assert.equal(validFilters(new URLSearchParams()),true);
console.log("Dashboard contract: malformed counts, duplicate rows, unavailable/empty states and filters PASS");
