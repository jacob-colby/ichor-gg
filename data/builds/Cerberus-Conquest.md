---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.67
  aspect_win_rate: 0.5
  slot_order:
  - name: Prophetic Cloak
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Book of Thoth
      pick_rate: 0.33
      win_rate: 0.0
    - name: Shifter's Shield
      pick_rate: 0.33
      win_rate: 0.0
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Bancroft's Talon
      pick_rate: 0.33
      win_rate: 0.0
    - name: Stampede
      pick_rate: 0.33
      win_rate: 0.0
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.33
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.33
      win_rate: 0.0
  - name: The Cosmic Horror
    pick_rate: 0.33
    win_rate: 0.0
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.33
      win_rate: 1.0
    - name: Sage's Ring
      pick_rate: 0.33
      win_rate: 0.0
  - name: Contagion
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Evil Eye
      pick_rate: 0.33
      win_rate: 0.0
    - name: Captain's Ring
      pick_rate: 0.33
      win_rate: 0.0
  - name: Shell of Rebuke
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.33
    win_rate: 1.0
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.0
  - name: Conduit Gem
    pick_rate: 0.33
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-11-04'
  god_win_rate: 0.3333333333333333
  god_matches_won: 1
  god_matches_played: 3
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  flex_slots:
  - Contagion
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Breastplate of Valor,
    Soul Gem, Nimble Ring, Erosion, Eye of Providence, Draconic Scale, Oni Hunter''s
    Garb, Helm of Darkness, Shield of the Phoenix, Stone of Binding, Helm of Radiance,
    Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Screeching
    Gargoyle, Spear of Desolation, Obsidian Shard, Ancile, Blood-Bound Book, Hide
    of the Nemean Lion.'
  slot_scores:
    Prophetic Cloak:
      total: 0.7
      efficiency: 0.44
      win: 1.0
      pick: 0.33
      fit: 0.51
    Shifter's Shield:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.57
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.67
    Contagion:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.71
      fit: 0.26
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.51
    Shell of Rebuke:
      total: 0.66
      efficiency: 0.29
      win: 1.0
      pick: 1.0
      fit: 0.4
  community_ordered:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  flex_slots:
  - Contagion
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Genji''s Guard, Blood-Bound Book, Phoenix Feather, Ethereal Staff, Yogi''s Necklace,
    Nimble Ring, Breastplate of Valor, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Chandra''s Grace, Draconic Scale, Midgardian Mail, Regrowth Striders, Helm of
    Radiance, Leviathan''s Hide, Glorious Pridwen, Helm of Darkness, Sphere of Negation,
    Spear of Desolation.'
  slot_scores:
    Prophetic Cloak:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.33
      fit: 0.45
    Shifter's Shield:
      total: 0.72
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.55
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.65
    Contagion:
      total: 0.67
      efficiency: 0.39
      win: 1.0
      pick: 0.71
      fit: 0.31
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.45
    Shell of Rebuke:
      total: 0.65
      efficiency: 0.29
      win: 1.0
      pick: 1.0
      fit: 0.34
  community_ordered:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  flex_slots:
  - Contagion
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Stone of Binding,
    Genji''s Guard, Screeching Gargoyle, Spear of Desolation, Obsidian Shard, Void
    Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Nimble Ring, Oni
    Hunter''s Garb, Erosion, Doom Orb, Eye of Providence, Helm of Radiance, The World
    Stone, Draconic Scale, Helm of Darkness, Shield of the Phoenix, Midgardian Mail,
    Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord.'
  slot_scores:
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.33
      fit: 0.38
    Shifter's Shield:
      total: 0.7
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.42
    Kinetic Cuirass:
      total: 0.75
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.52
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.71
      fit: 0.22
    Freya's Tears:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.38
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.29
      win: 1.0
      pick: 1.0
      fit: 0.3
  community_ordered:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Shifter's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Bragi's Harp
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Nimble Ring, Gluttonous Grimoire, Breastplate
    of Valor, Soul Gem, Oni Hunter''s Garb, Helm of Radiance, Erosion, Eye of Providence,
    Obsidian Shard, Stone of Binding, Spear of Desolation, Helm of Darkness, Midgardian
    Mail, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Screeching Gargoyle,
    Blood-Bound Book, Leviathan''s Hide, Bragi''s Harp, Mantle Of Discord, Ancient
    Signet, Bracer of The Abyss.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.22
      efficiency: 0.52
      win: 0.0
      pick: 0.0
      fit: 0.24
    Shifter's Shield:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.36
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.46
    Nimble Ring:
      total: 0.27
      efficiency: 0.63
      win: 0.0
      pick: 0.0
      fit: 0.31
    Freya's Tears:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.33
    Bragi's Harp:
      total: 0.22
      efficiency: 0.45
      win: 0.0
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Shifter's Shield
  - Prophetic Cloak
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  flex_slots:
  - Contagion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Amanita Charm, Soul
    Gem, Breastplate of Valor, Spear of Desolation, Gluttonous Grimoire, Shield of
    the Phoenix, Screeching Gargoyle, Nimble Ring, Chronos'' Pendant, Helm of Radiance,
    Oni Hunter''s Garb, Helm of Darkness, Obsidian Shard, Erosion, Eye of Providence,
    Stone of Binding, Draconic Scale, Midgardian Mail, Blood-Bound Book, Gem of Focus,
    Gladiator''s Shield, Magi''s Cloak, Heartwood Charm, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.3
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.39
    Prophetic Cloak:
      total: 0.7
      efficiency: 0.44
      win: 1.0
      pick: 0.33
      fit: 0.55
    Kinetic Cuirass:
      total: 0.75
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.49
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.71
      fit: 0.21
    Freya's Tears:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.55
  community_ordered:
  - Shifter's Shield
  - Prophetic Cloak
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  flex_slots:
  - Contagion
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Amanita
    Charm, Shield Splitter, Gluttonous Grimoire, Genji''s Guard, Soul Gem, Runeforged
    Hammer, The Reaper, Tekko-Kagi, Titan''s Bane, Golden Blade, Nimble Ring, Breastplate
    of Valor, Hydra''s Lament, Obsidian Shard, Spear of Desolation, Tyrfing, The Crusher,
    Oni Hunter''s Garb, Helm of Radiance, Lernaean Bow, Erosion, Avenging Blade, Eye
    of Providence, Heartseeker, Stone of Binding, Draconic Scale, Helm of Darkness,
    Shield of the Phoenix, Midgardian Mail, Arondight, Spear of the Magus, Death Metal,
    Magi''s Cloak, Toxic Blade, Screeching Gargoyle, Pharaoh''s Curse.'
  slot_scores:
    Prophetic Cloak:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.33
      fit: 0.35
    Shifter's Shield:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.38
    Kinetic Cuirass:
      total: 0.75
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.48
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.71
      fit: 0.21
    Freya's Tears:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.35
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.29
      win: 1.0
      pick: 1.0
      fit: 0.27
  community_ordered:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  flex_slots:
  - Contagion
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Genji''s Guard, Shield Splitter, Nimble
    Ring, Obsidian Shard, Spear of Desolation, Helm of Radiance, Runeforged Hammer,
    Breastplate of Valor, The Reaper, Titan''s Bane, Tekko-Kagi, Helm of Darkness,
    Spear of the Magus, Hydra''s Lament, Golden Blade, Blood-Bound Book, Death Metal,
    Oni Hunter''s Garb, Ancient Signet, Erosion, Tyrfing, Eye of Providence, The Crusher,
    Jade Scepter, Stone of Binding, Doom Orb, Midgardian Mail, Draconic Scale, Bragi''s
    Harp, Shield of the Phoenix, Avenging Blade, Lernaean Bow, The World Stone.'
  slot_scores:
    Prophetic Cloak:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.33
      fit: 0.33
    Shifter's Shield:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.45
      fit: 0.36
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.46
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.71
      fit: 0.2
    Freya's Tears:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.33
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.29
      win: 1.0
      pick: 1.0
      fit: 0.26
  community_ordered:
  - Prophetic Cloak
  - Shifter's Shield
  - Kinetic Cuirass
  - Contagion
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Breastplate
    of Valor, Soul Gem, Nimble Ring, Erosion, Eye of Providence, Draconic Scale, Oni
    Hunter''s Garb, Helm of Darkness, Shield of the Phoenix, Stone of Binding, Helm
    of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Leviathan''s Hide,
    Screeching Gargoyle, Spear of Desolation, Obsidian Shard, Ancile, Blood-Bound
    Book, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.29
      efficiency: 0.69
      win: 0.0
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.27
      efficiency: 0.63
      win: 0.0
      pick: 0.0
      fit: 0.31
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.51
      fit: 0.51
    Kinetic Cuirass:
      total: 0.77
      efficiency: 0.56
      win: 1.0
      pick: 0.55
      fit: 0.67
    Amanita Charm:
      total: 0.31
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.57
    Erosion:
      total: 0.26
      efficiency: 0.51
      win: 0.0
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
---
