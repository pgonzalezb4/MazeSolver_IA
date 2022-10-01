import cytoscape from "cytoscape";
import { MazeCoordinate, Path } from "./maze-drawer";

export interface Node {
  data: { id: string };
}

export interface Edge {
  data: {
    id: string;
    weight: number;
    source: string;
    target: string;
  };
}

export class GraphDrawer {
  private tree: unknown[] = [];
  private cy: cytoscape.Core | undefined;

  constructor(private container: HTMLDivElement) {}

  initialize(nodes: MazeCoordinate[], edges: Path[], roots: MazeCoordinate[]) {
    this.cy = cytoscape({
      container: this.container,

      boxSelectionEnabled: false,
      autounselectify: true,

      style: cytoscape
        .stylesheet()
        .selector("node")
        .style({
          content: "data(id)",
        })
        .selector("edge")
        .style({
          "curve-style": "bezier",
          "target-arrow-shape": "triangle",
          width: 4,
          "line-color": "#11241A",
          "target-arrow-color": "#11241A",
        })
        .selector(".highlighted")
        .style({
          "background-color": "#FFD700",
          "line-color": "#FFD700",
          "target-arrow-color": "#FFD700",
          "transition-property":
            "background-color, line-color, target-arrow-color",
          "transition-duration": "0.3s",
        })
        .selector(".highlighted-bad")
        .style({
          "background-color": "#ED2939",
          "line-color": "#ED2939",
          "target-arrow-color": "#ED2939",
          "transition-property":
            "background-color, line-color, target-arrow-color",
          "transition-duration": "0.1s",
        }),

      elements: {
        nodes: nodes.map(([y, x]) => ({
          data: {
            id: `${y}${x}`,
          },
          grabbable: false,
        })),
        edges: edges.flatMap(([source, target]) => [
          {
            data: {
              id: `${source}_${target}`.replaceAll(",", ""),
              weight: 1,
              source: `${source}`.replaceAll(",", ""),
              target: `${target}`.replaceAll(",", ""),
            },
          },
          {
            data: {
              id: `${target}_${source}`.replaceAll(",", ""),
              weight: 1,
              source: `${target}`.replaceAll(",", ""),
              target: `${source}`.replaceAll(",", ""),
            },
          }
        ]),
      },

      layout: {
        name: "breadthfirst",
        directed: false,
        padding: 10,
        roots: `#${roots[0]}`.replaceAll(",", ""),
        avoidOverlap: true,
        spacingFactor: 3,
      },

      userPanningEnabled: true,
      userZoomingEnabled: true,
    });

    return this;
  }

  async drawPath(explorationPaths: Path[], path: Path) {
    for (const path of explorationPaths) {
      this.cy?.center(this.cy.elements());
      this.cy?.minZoom();

      for (let i = 1; i < path.length; i++) {
        const [source, target] = [path[i - 1], path[i]];

        this.cy
          ?.nodes(`#${source}`.replaceAll(",", ""))
          .addClass("highlighted-bad");
        this.cy
          ?.nodes(`#${target}`.replaceAll(",", ""))
          .addClass("highlighted-bad");
        this.cy
          ?.edges(`#${source}_${target}`.replaceAll(",", ""))
          .addClass("highlighted-bad");
      }

      await new Promise((resolve) => setTimeout(resolve, 100));
    }

    for (let i = 1; i < path.length; i++) {
      const [source, target] = [path[i - 1], path[i]];

      this.cy
        ?.nodes(`#${source}`.replaceAll(",", ""))
        .classes([])
        .addClass("highlighted");
      this.cy
        ?.nodes(`#${target}`.replaceAll(",", ""))
        .classes([])
        .addClass("highlighted");
      this.cy
        ?.edges(`#${source}_${target}`.replaceAll(",", ""))
        .classes([])
        .addClass("highlighted");

      await new Promise((resolve) => setTimeout(resolve, 200));
    }
  }
}
