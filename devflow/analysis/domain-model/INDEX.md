# Domain Model — Index

**Methodology version:** 5.0

Readable domain model: entities, relationships and enumerations.

---

## Entities

| Entity | Label | Module | Status |
|--------|-------|--------|--------|
| [InputKit](entities/InputKit.md) | Kit de entrada (AvengaDevFlow) | metaflow-transform | stable |
| [DistributionKit](entities/DistributionKit.md) | Kit de salida (MetaFlow) | metaflow-transform | stable |
| [MappingRule](entities/MappingRule.md) | Regla de transformación | metaflow-transform | stable |
| [TransformRun](entities/TransformRun.md) | Ejecución de transformación | metaflow-transform | stable |

> Status: `draft` | `stable` | `deprecated`.

---

## Enumerations

| Enum | Label | Module | Status |
|------|-------|--------|--------|
| [RuleType](enumerations/RuleType.md) | Tipo de regla de transformación | metaflow-transform | stable |

---

## Relationships

| Document | Purpose |
|----------|----------|
| [metaflow-transform.md](relationships/metaflow-transform.md) | Catálogo de relaciones del pipeline de transformación (InputKit → TransformRun → DistributionKit, MappingTable → MappingRule) |
| [relationships/TEMPLATE-RELATIONSHIP.md](relationships/TEMPLATE-RELATIONSHIP.md) | Template for module-specific relationship catalogs |

> Create one file per module/bounded context using the template. See
> [relationships/README.md](relationships/README.md) for conventions.

---

**Last updated:** August 2026
