---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.38
    win_rate: 0.67
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.13
      win_rate: 0.0
    - name: Transcendence
      pick_rate: 0.13
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.5
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.25
      win_rate: 0.0
    - name: Contagion
      pick_rate: 0.13
      win_rate: 0.0
  - name: Breastplate of Valor
    pick_rate: 0.38
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.38
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.0
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.0
    - name: Shield of the Phoenix
      pick_rate: 0.13
      win_rate: 0.0
  - name: Brawler’s Beat Stick
    pick_rate: 0.25
    win_rate: 0.5
    alternates:
    - name: Void Shield
      pick_rate: 0.13
      win_rate: 0.0
    - name: Wyrmskin Hide
      pick_rate: 0.13
      win_rate: 0.0
  - name: Hide of the Nemean Lion
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Sundering Echo
      pick_rate: 0.17
      win_rate: 1.0
    - name: Medal of Defense
      pick_rate: 0.17
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.63
    win_rate: 0.4
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.5
  - name: Blood-soaked Shroud
    pick_rate: 0.13
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-09'
  god_win_rate: 0.375
  god_matches_won: 3
  god_matches_played: 8
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Brawler’s Beat Stick
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  flex_slots:
  - Brawler’s Beat Stick
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging
    Blade, Gluttonous Grimoire, Lernaean Bow, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Heartseeker, Draconic Scale, Shogun''s Ofuda, Golden
    Blade, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring,
    Helm of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance,
    Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter,
    The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.17
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.59
      fit: 0.17
    Brawler’s Beat Stick:
      total: 0.44
      efficiency: 0.42
      win: 0.5
      pick: 0.54
      fit: 0.25
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.22
      fit: 0.25
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.38
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 1.0
      fit: 0.32
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Brawler’s Beat Stick
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Brawler’s Beat Stick
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  flex_slots:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Kinetic Cuirass, Runeforged Hammer, Rod of Asclepius, Shield Splitter, Eye of
    the Storm, Soul Gem, Erosion, Ethereal Staff, The Reaper, Eye of Providence, Yogi''s
    Necklace, Draconic Scale, Phoenix Feather, Gluttonous Grimoire, Avenging Blade,
    Pharaoh''s Curse, Shogun''s Ofuda, Lernaean Bow, Hydra''s Lament, Lifebinder,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Chandra''s Grace, Daybreak
    Gavel, Magi''s Cloak, Leviathan''s Hide, Sphere of Negation, Stampede, Heartseeker,
    Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.2
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.59
      fit: 0.2
    Brawler’s Beat Stick:
      total: 0.45
      efficiency: 0.42
      win: 0.5
      pick: 0.54
      fit: 0.33
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.22
      fit: 0.33
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.38
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 1.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Brawler’s Beat Stick
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Brawler’s Beat Stick
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  flex_slots:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear of the Magus, Runeforged
    Hammer, Stone of Binding, Obsidian Shard, Spear of Desolation, Tekko-Kagi, Titan''s
    Bane, Kinetic Cuirass, The Crusher, Soul Gem, Screeching Gargoyle, The Reaper,
    Void Stone, Shield Splitter, Doom Orb, Eye of the Storm, The World Stone, Avatar''s
    Parashu, Hydra''s Lament, Lernaean Bow, Dreamer''s Idol, Pendulum Blade, Nimble
    Ring, Daybreak Gavel, Helm of Radiance, Erosion, Pharaoh''s Curse, Rod of Asclepius,
    Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.12
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.65
      win: 0.33
      pick: 0.59
      fit: 0.12
    Brawler’s Beat Stick:
      total: 0.43
      efficiency: 0.42
      win: 0.5
      pick: 0.54
      fit: 0.17
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.22
      fit: 0.17
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.38
      fit: 0.31
    Hide of the Nemean Lion:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 1.0
      fit: 0.22
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Brawler’s Beat Stick
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Shifter's Shield
  - Shell of Rebuke
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Nimble Ring, Golden Blade, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Tyrfing, Runeforged Hammer, Riptalon,
    Kinetic Cuirass, Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s Curse,
    Soul Gem, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi, Bragi''s Harp, Eye of
    the Storm, Hydra''s Lament, The Reaper, Daybreak Gavel, Dominance, Avenging Blade,
    Helm of Radiance, Bracer of The Abyss, Rod of Asclepius, Spear of the Magus, Erosion,
    Eye of Providence, Qin''s Blade, Vital Amplifier, Heartseeker, Draconic Scale,
    Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.28
      efficiency: 0.52
      win: 0.0
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.11
    Berserker's Shield:
      total: 0.31
      efficiency: 0.68
      win: 0.0
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.28
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.36
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.38
      fit: 0.29
    Shell of Rebuke:
      total: 0.58
      efficiency: 0.28
      win: 1.0
      pick: 0.22
      fit: 0.16
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Berserker''s Shield, Amanita Charm, Spear of Desolation, Hydra''s Lament, Soul
    Gem, Chronos'' Pendant, Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer,
    Gluttonous Grimoire, Arondight, Gem of Focus, Gladiator''s Shield, Nimble Ring,
    Eye of Erebus, Helm of Radiance, Rod of Asclepius, Shield Splitter, Spear of the
    Magus, Chandra''s Grace, Eye of the Storm, Daybreak Gavel, Obsidian Shard, Erosion,
    Pharaoh''s Curse, Jade Scepter, Lernaean Bow, Eye of Providence, Wish-Granting
    Pearl, Avenging Blade, Totem of Death, Draconic Scale, Pendulum Blade, Shogun''s
    Ofuda.'
  slot_scores:
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.33
      pick: 0.59
      fit: 0.44
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.34
      fit: 0.44
    Jotunn's Revenge:
      total: 0.32
      efficiency: 0.72
      win: 0.0
      pick: 0.0
      fit: 0.49
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.22
      fit: 0.17
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.38
      fit: 0.31
    Hide of the Nemean Lion:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 1.0
      fit: 0.23
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Hydra''s Lament, Erosion,
    Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic Scale, Shogun''s Ofuda,
    Golden Blade, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble
    Ring, Helm of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance,
    Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter,
    The Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.31
      efficiency: 0.68
      win: 0.0
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.31
      efficiency: 0.72
      win: 0.0
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.28
      efficiency: 0.56
      win: 0.0
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.27
      efficiency: 0.55
      win: 0.0
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.29
      efficiency: 0.57
      win: 0.0
      pick: 0.13
      fit: 0.56
    Amanita Charm:
      total: 0.3
      efficiency: 0.65
      win: 0.0
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Runeforged Hammer
  starter: *id001
---
