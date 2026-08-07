---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.52
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.53
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.59
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.45
  - name: Spirit Robe
    pick_rate: 0.1
    win_rate: 0.47
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.55
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.56
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.74
    alternates:
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.53
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.73
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.19
    win_rate: 0.57
  - name: Selflessness
    pick_rate: 0.18
    win_rate: 0.44
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-07'
  god_win_rate: 0.5183333333333333
  god_matches_won: 311
  god_matches_played: 600
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Breastplate of Valor,
    Freya''s Tears, Oni Hunter''s Garb, Erosion, Gluttonous Grimoire, Shield of the
    Phoenix, Hide of the Nemean Lion, Draconic Scale, Spectral Armor, Leviathan''s
    Hide, Stampede, Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s
    Necklace, Helm of Radiance, Soul Gem, Magi''s Cloak, Rod of Asclepius, Ancile,
    Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.11
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.25
      fit: 0.72
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Breastplate of Valor, Rod of Asclepius, Oni Hunter''s Garb, Gluttonous Grimoire,
    Soul Gem, Chandra''s Grace, Freya''s Tears, Hide of the Nemean Lion, Erosion,
    Draconic Scale, Phoenix Feather, Spectral Armor, Lifebinder, Leviathan''s Hide,
    Yogi''s Necklace, Stampede, Midgardian Mail, Blood-Bound Book, Bancroft''s Talon,
    Glorious Pridwen, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.35
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.25
      fit: 0.7
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Eye of Providence
  - Shifter's Shield
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
    for this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Soul Gem, Eye of Providence, Stone of Binding, Oni Hunter''s Garb, Spear
    of the Magus, Screeching Gargoyle, Freya''s Tears, Void Shield, The Cosmic Horror,
    Void Stone, Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor,
    Draconic Scale, Obsidian Shard, Yogi''s Necklace, Leviathan''s Hide, Helm of Radiance,
    Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.25
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.11
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.25
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, Freya''s Tears, Hide of the Nemean Lion,
    Soul Gem, Shield of the Phoenix, Spectral Armor, Yogi''s Necklace, Erosion, Bracer
    of The Abyss, Draconic Scale, Death Metal, Helm of Radiance, Rod of Asclepius,
    Leviathan''s Hide, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Stone of
    Binding, Jade Scepter, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.2
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.11
      fit: 0.2
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Freya''s Tears,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Eye of Providence, Soul
    Gem, Gluttonous Grimoire, Oni Hunter''s Garb, Chronos'' Pendant, Screeching Gargoyle,
    Chandra''s Grace, Gladiator''s Shield, Spectral Armor, Erosion, Spear of Desolation,
    Yogi''s Necklace, Prophetic Cloak, Draconic Scale, Helm of Radiance, Rod of Asclepius,
    Gem of Focus, Death Metal, Leviathan''s Hide, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.11
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Breastplate of Valor, Kinetic Cuirass,
    Eye of Providence, Runeforged Hammer, Hydra''s Lament, Oni Hunter''s Garb, Shield
    Splitter, Soul Gem, Freya''s Tears, Golden Blade, Lernaean Bow, Eye of the Storm,
    Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor, Avenging
    Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Spear of the Magus, Draconic
    Scale, Shogun''s Ofuda, Leviathan''s Hide, The Cosmic Horror, Dominance, Helm
    of Radiance, Rod of Asclepius, Heartseeker, Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Amanita Charm, Breastplate of Valor, The Crusher, Jotunn''s Revenge, Kinetic
    Cuirass, Soul Gem, Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s
    Lament, Death Metal, Freya''s Tears, Spear of the Magus, Shield Splitter, The
    Cosmic Horror, Helm of Radiance, Rod of Asclepius, Shield of the Phoenix, Eye
    of the Storm, Pharaoh''s Curse, Spectral Armor, Yogi''s Necklace, Erosion, Jade
    Scepter, Golden Blade, Spear of Desolation, Lernaean Bow, Avenging Blade, Draconic
    Scale, Obsidian Shard, The Reaper, Damaru, Chronos'' Pendant, Triton''s Conch,
    Leviathan''s Hide, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.3
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Freya''s
    Tears, Oni Hunter''s Garb, Erosion, Gluttonous Grimoire, Shield of the Phoenix,
    Breastplate of Valor, Draconic Scale, Spectral Armor, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of the Nemean
    Lion, Helm of Radiance, Soul Gem, Magi''s Cloak, Rod of Asclepius, Stampede, Ancile,
    Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.25
      fit: 0.72
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
---
