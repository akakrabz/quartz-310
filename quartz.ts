import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"

// Order the Explorer ("Course map") by file/folder *name* instead of by title,
// so the numeric prefixes (0-midterm-1, 0-toolkit, 1-…, 2-…, 01-…, 02-…) fix the
// order while the visible titles stay clean.
//
// The generated plugin index re-exports npm components directly, so calling
// ExternalPlugin.Explorer({ sortFn }) here would NOT reach the layout; the option
// override has to be registered under the plugin's source string instead.
//
// NOTE: this function is serialized with .toString() and re-run in the browser,
// so it must stay self-contained (no imports, no outer variables).
componentRegistry.setOptionOverrides("@quartz-community/explorer", {
  sortFn: (a: any, b: any) => {
    if (a.isFolder !== b.isFolder) {
      return a.isFolder ? -1 : 1
    }
    return (a.slugSegment ?? "").localeCompare(b.slugSegment ?? "", undefined, {
      numeric: true,
      sensitivity: "base",
    })
  },
  // .canvas / .base pages have no frontmatter title; give them readable names
  mapFn: (node: any) => {
    const names: Record<string, string> = {
      "concept-map": "Concept map (canvas)",
      "concept-map.canvas": "Concept map (canvas)",
      "exam-problem-families": "Problem-family table",
      "exam-problem-families.base": "Problem-family table",
    }
    if (names[node.displayName]) node.displayName = names[node.displayName]
    return node
  },
})

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
