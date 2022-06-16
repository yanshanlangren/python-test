#!/usr/bin/env bash
data=`curl -s localhost:{{getv "/env/nifi_web_http_port" "8080"}}/nifi-api/system-diagnostics/|jq '.systemDiagnostics.aggregateSnapshot'`

heapUtilization=`echo $data|jq '.heapUtilization'|cut -b 2-5`
flowFileRepositoryUtilization=`echo $data|jq '.flowFileRepositoryStorageUsage.utilization'|cut -b 2-5`
contentRepositoryUtilization=`echo $data|jq '.contentRepositoryStorageUsage[0].utilization'|cut -b 2-5`
provenanceRepositoryStorageUtilization=`echo $data|jq '.provenanceRepositoryStorageUsage[0].utilization'|cut -b 2-5`

total_non_heap=$(echo `echo $data|jq '.totalNonHeapBytes'`/1048576|bc)
used_non_heap=$(echo `echo $data|jq '.usedNonHeapBytes'`/1048576|bc)
free_non_heap=$(echo `echo $data|jq '.freeNonHeapBytes'`/1048576|bc)
max_non_heap=$(echo `echo $data|jq '.maxNonHeapBytes'`/1048576|bc)
total_heap=$(echo `echo $data|jq '.totalHeapBytes'`/1048576|bc)
free_heap=$(echo `echo $data|jq '.freeHeapBytes'`/1048576|bc)
max_heap=$(echo `echo $data|jq '.maxHeapBytes'`/1048576|bc)
total_flow_file_repository_storage=$(echo `echo $data|jq '.flowFileRepositoryStorageUsage.totalSpaceBytes'`/1048576|bc)
total_content_repository_storage=$(echo `echo $data|jq '.contentRepositoryStorageUsage[0].totalSpaceBytes'`/1048576|bc)
total_provenance_repository_storage=$(echo `echo $data|jq '.provenanceRepositoryStorageUsage[0].totalSpaceBytes'`/1048576|bc)
used_heap=$(echo `echo $data|jq '.usedHeapBytes'`/1048576|bc)

ret=`echo $data|jq '.|{available_processors:.availableProcessors, processor_load_average:.processorLoadAverage,total_threads:.totalThreads,daemon_threads:.daemonThreads}'`
cat <<EOF
${ret:0:-2},"heap_utilization":$heapUtilization,"content_repository_storage_utilization":$contentRepositoryUtilization,"flow_file_repository_storage_utilization":$flowFileRepositoryUtilization,"provenance_repository_storage_utilization":$provenanceRepositoryStorageUtilization,"total_non_heap":$total_non_heap,"used_non_heap":$used_non_heap,"free_non_heap":$free_non_heap,"max_non_heap":$max_non_heap,"total_heap":$total_heap,"free_heap":$free_heap,"max_heap":$max_heap,"total_flow_file_repository_storage":$total_flow_file_repository_storage,"total_content_repository_storage":$total_content_repository_storage,"total_provenance_repository_storage":$total_provenance_repository_storage,"used_heap":$used_heap}
EOF
