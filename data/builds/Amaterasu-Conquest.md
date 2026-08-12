---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.42
    win_rate: 0.63
    alternates:
    - name: Golden Blade
      pick_rate: 0.3
      win_rate: 0.64
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.52
  - name: Berserker's Shield
    pick_rate: 0.21
    win_rate: 0.57
    alternates:
    - name: Golden Blade
      pick_rate: 0.17
      win_rate: 0.73
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.63
  - name: Kinetic Cuirass
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.21
      win_rate: 0.63
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.65
  - name: Shogun's Ofuda
    pick_rate: 0.17
    win_rate: 0.6
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.18
      win_rate: 0.58
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.88
  - name: Olmec Blue
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.31
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.69
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.39
    win_rate: 0.59
  - name: Death's Toll
    pick_rate: 0.23
    win_rate: 0.61
  - name: Archmage's Gem
    pick_rate: 0.08
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-08-11'
  god_win_rate: 0.6151898734177215
  god_matches_won: 243
  god_matches_played: 395
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Hide of the Nemean Lion, Amanita Charm, Eye of Providence,
    Genji''s Guard, Gluttonous Grimoire, Jotunn''s Revenge, Freya''s Tears, Oni Hunter''s
    Garb, Runeforged Hammer, The Crusher, Shield Splitter, Breastplate of Valor, Hydra''s
    Lament, Shield of the Phoenix, Eye of the Storm, Erosion, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Soul Gem, Yogi''s Necklace, Avenging Blade, Death Metal,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Helm
    of Radiance, Lernaean Bow, Rod of Asclepius, Damaru, Stampede, Magi''s Cloak,
    Ancile, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.3
      fit: 0.37
    Berserker's Shield:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.36
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.67
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.54
      win: 0.69
      pick: 0.06
      fit: 0.36
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Hide of the Nemean Lion, Shield of the
    Phoenix, Soul Gem, Eye of Providence, Genji''s Guard, Gluttonous Grimoire, Rod
    of Asclepius, Runeforged Hammer, Jotunn''s Revenge, Oni Hunter''s Garb, Chandra''s
    Grace, The Crusher, Hydra''s Lament, Freya''s Tears, Breastplate of Valor, The
    Reaper, Eye of the Storm, Shield Splitter, Erosion, Phoenix Feather, Spectral
    Armor, Avenging Blade, Draconic Scale, Pharaoh''s Curse, Blood-Bound Book, Yogi''s
    Necklace, Lifebinder, Bancroft''s Talon, Leviathan''s Hide, Death Metal, Riptalon,
    Midgardian Mail, Lernaean Bow, Glorious Pridwen.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.3
      fit: 0.43
    Berserker's Shield:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.38
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.65
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.54
      win: 0.69
      pick: 0.06
      fit: 0.38
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Gluttonous Grimoire
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Amanita Charm, Genji''s Guard, Soul Gem, Avenging Blade, Eye of Providence, Stone
    of Binding, Oni Hunter''s Garb, Screeching Gargoyle, Runeforged Hammer, Breastplate
    of Valor, Hydra''s Lament, Freya''s Tears, Void Shield, Spear of the Magus, Shield
    Splitter, The Reaper, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Spectral Armor, Eye of the Storm, Erosion, Yogi''s Necklace, Heartseeker,
    Pharaoh''s Curse, Riptalon, Draconic Scale, Obsidian Shard, Death Metal, Leviathan''s
    Hide, Silverbranch Bow, Lernaean Bow.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.3
      fit: 0.27
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.69
      pick: 0.06
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Shogun's Ofuda
  flex_slots:
  - Hide of the Nemean Lion
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Genji''s Guard, Gluttonous Grimoire,
    Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher, Jotunn''s
    Revenge, Breastplate of Valor, Riptalon, Freya''s Tears, Runeforged Hammer, Hydra''s
    Lament, Lernaean Bow, Soul Gem, Shield of the Phoenix, Tyrfing, Spectral Armor,
    Silverbranch Bow, Yogi''s Necklace, Shield Splitter, Erosion, Eye of the Storm,
    Bracer of The Abyss, Draconic Scale, Dominance, Death Metal, Leviathan''s Hide,
    Rod of Asclepius, Helm of Radiance, Avenging Blade, Bragi''s Harp, Midgardian
    Mail, Damaru, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.55
      win: 0.64
      pick: 0.3
      fit: 0.53
    Berserker's Shield:
      total: 0.58
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.46
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.69
      pick: 0.06
      fit: 0.23
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.36
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.17
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Hide
    of the Nemean Lion, Freya''s Tears, Breastplate of Valor, Amanita Charm, Jotunn''s
    Revenge, Shield of the Phoenix, Hydra''s Lament, Soul Gem, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, The Crusher, Chronos'' Pendant, Runeforged
    Hammer, Screeching Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s
    Shield, Spectral Armor, Erosion, Shield Splitter, Yogi''s Necklace, Pharaoh''s
    Curse, Prophetic Cloak, Draconic Scale, Helm of Radiance, Rod of Asclepius, Gem
    of Focus, Eye of the Storm, Arondight, Death Metal, Leviathan''s Hide, Jade Scepter,
    Midgardian Mail, Spear of the Magus, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.56
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.29
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Hide of the Nemean Lion
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire, Soul
    Gem, Amanita Charm, Genji''s Guard, Jotunn''s Revenge, The Crusher, Eye of Providence,
    Breastplate of Valor, Oni Hunter''s Garb, Hydra''s Lament, Freya''s Tears, Spear
    of the Magus, Runeforged Hammer, Death Metal, The Cosmic Horror, Helm of Radiance,
    Rod of Asclepius, Shield of the Phoenix, Spear of Desolation, Shield Splitter,
    Jade Scepter, Spectral Armor, Chronos'' Pendant, Yogi''s Necklace, Eye of the
    Storm, Erosion, Obsidian Shard, Pharaoh''s Curse, Wish-Granting Pearl, Blood-Bound
    Book, Draconic Scale, Ethereal Staff, Triton''s Conch, Bancroft''s Talon, Avenging
    Blade, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.3
      fit: 0.26
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.49
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.69
      pick: 0.06
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire,
    Amanita Charm, Jotunn''s Revenge, The Crusher, Genji''s Guard, Soul Gem, Eye of
    Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament, Breastplate
    of Valor, Freya''s Tears, Death Metal, Spear of the Magus, Shield Splitter, Shield
    of the Phoenix, The Cosmic Horror, Helm of Radiance, Rod of Asclepius, Eye of
    the Storm, Spectral Armor, Spear of Desolation, Erosion, Yogi''s Necklace, Jade
    Scepter, Pharaoh''s Curse, Avenging Blade, Draconic Scale, Obsidian Shard, Chronos''
    Pendant, Lernaean Bow, The Reaper, Triton''s Conch, Damaru, Leviathan''s Hide,
    Wish-Granting Pearl.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.3
      fit: 0.29
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.26
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.51
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.69
      pick: 0.06
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.42
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Genji''s
    Guard, Gluttonous Grimoire, Jotunn''s Revenge, Freya''s Tears, Oni Hunter''s Garb,
    Runeforged Hammer, The Crusher, Shield Splitter, Breastplate of Valor, Hydra''s
    Lament, Shield of the Phoenix, Eye of the Storm, Erosion, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Soul Gem, Yogi''s Necklace, Avenging Blade, Death Metal,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Hide
    of the Nemean Lion, Helm of Radiance, Lernaean Bow, Rod of Asclepius, Damaru,
    Stampede, Magi''s Cloak, Ancile, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.32
    Berserker's Shield:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.21
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.64
      pick: 0.12
      fit: 0.67
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
