---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.57
  aspect_win_rate: 0.61
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.81
    win_rate: 0.6
    alternates:
    - name: Tyrfing
      pick_rate: 0.08
      win_rate: 0.6
    - name: Daybreak Gavel
      pick_rate: 0.04
      win_rate: 0.59
  - name: Vital Amplifier
    pick_rate: 0.32
    win_rate: 0.6
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.26
      win_rate: 0.64
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.63
  - name: Riptalon
    pick_rate: 0.24
    win_rate: 0.59
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.17
      win_rate: 0.57
    - name: Gluttonous Grimoire
      pick_rate: 0.07
      win_rate: 0.71
  - name: Gluttonous Grimoire
    pick_rate: 0.19
    win_rate: 0.64
    alternates:
    - name: Riptalon
      pick_rate: 0.22
      win_rate: 0.64
    - name: Silverbranch Bow
      pick_rate: 0.06
      win_rate: 0.67
  - name: Silverbranch Bow
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Riptalon
      pick_rate: 0.18
      win_rate: 0.63
    - name: Gluttonous Grimoire
      pick_rate: 0.09
      win_rate: 0.66
  - name: Blinking Abyss
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.05
      win_rate: 0.62
    - name: Manchu Bow
      pick_rate: 0.05
      win_rate: 0.46
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.47
    win_rate: 0.66
  - name: Leather Cowl
    pick_rate: 0.21
    win_rate: 0.47
  - name: Death's Embrace
    pick_rate: 0.11
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-09-30'
  god_win_rate: 0.5964071856287425
  god_matches_won: 498
  god_matches_played: 835
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-30'
  god_matches_analyzed: 9423
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Silverbranch Bow, Spear of Desolation, Spear of the Magus, Obsidian Shard, Lernaean
    Bow, Tyrfing, The Reaper, Tekko-Kagi, Bragi''s Harp, Hydra''s Lament, Heartseeker,
    Bracer of The Abyss, Deathbringer, Doom Orb, Golden Blade, Chronos'' Pendant,
    Titan''s Bane, The World Stone, Dominance, The Crusher, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Demon Blade, Toxic Blade, Musashi''s Dual Swords, Bancroft''s
    Talon, Arondight, Gem of Focus, Transcendence, Pendulum Blade, Runeforged Hammer,
    Avatar''s Parashu, Qin''s Blade, Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.32
      fit: 0.47
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.65
      pick: 0.13
      fit: 0.42
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.29
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Gluttonous Grimoire
  - Silverbranch Bow
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Silverbranch
    Bow, Spear of Desolation, Spear of the Magus, Hydra''s Lament, Obsidian Shard,
    Bragi''s Harp, Lernaean Bow, Heartseeker, The Reaper, Tyrfing, Tekko-Kagi, Doom
    Orb, Ancient Signet, The World Stone, Bracer of The Abyss, Chronos'' Pendant,
    Dominance, Deathbringer, Bancroft''s Talon, Golden Blade, Titan''s Bane, Blood-Bound
    Book, The Crusher, Dreamer''s Idol, Transcendence, Arondight, Gem of Focus, Book
    of Thoth, Musashi''s Dual Swords, Polynomicon, Demon Blade, Runeforged Hammer,
    Rod of Asclepius, Soul Reaver, Pendulum Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.32
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Musashi's Dual Swords
  - Deathbringer
  - Rod of Tahuti
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem,
    Silverbranch Bow, Spear of Desolation, Spear of the Magus, Obsidian Shard, The
    Reaper, Lernaean Bow, Tyrfing, Tekko-Kagi, Bragi''s Harp, Hydra''s Lament, Heartseeker,
    Bracer of The Abyss, Deathbringer, Doom Orb, Chronos'' Pendant, The World Stone,
    Ancient Signet, Golden Blade, Blood-Bound Book, Dreamer''s Idol, Titan''s Bane,
    The Crusher, Dominance, Musashi''s Dual Swords, Demon Blade, Toxic Blade, Bancroft''s
    Talon, Gem of Focus, Arondight, Transcendence, Damaru, Rage, Pendulum Blade, Rod
    of Asclepius, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.32
      fit: 0.47
    Musashi's Dual Swords:
      total: 0.49
      efficiency: 0.46
      win: 0.61
      pick: 0.0
      fit: 0.36
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Silverbranch
    Bow, Spear of Desolation, Spear of the Magus, Obsidian Shard, The Reaper, Tekko-Kagi,
    Hydra''s Lament, Heartseeker, Lernaean Bow, Tyrfing, Bragi''s Harp, Doom Orb,
    Chronos'' Pendant, The World Stone, Titan''s Bane, The Crusher, Bracer of The
    Abyss, Dreamer''s Idol, Deathbringer, Ancient Signet, Golden Blade, Toxic Blade,
    Blood-Bound Book, Pendulum Blade, Dominance, Arondight, Gem of Focus, Bancroft''s
    Talon, Avatar''s Parashu, Musashi''s Dual Swords, The Cosmic Horror, Demon Blade,
    Transcendence, Runeforged Hammer, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.13
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.32
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Jotunn''s Revenge, Berserker''s
    Shield, The Reaper, Rod of Asclepius, Nimble Ring, Shield of the Phoenix, Death
    Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Silverbranch Bow, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Bancroft''s Talon, Runeforged Hammer,
    Golden Blade, Yogi''s Necklace, Spear of the Magus, Spear of Desolation, Lifebinder,
    Helm of Radiance, Obsidian Shard, Shifter''s Shield, Shield Splitter, Lernaean
    Bow, Sphere of Negation, Hydra''s Lament, Pharaoh''s Curse, Tyrfing, Chandra''s
    Grace, Phoenix Feather, Eye of the Storm, Heartseeker, Shogun''s Ofuda, Tekko-Kagi,
    Bragi''s Harp.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.27
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.32
      fit: 0.47
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Silverbranch Bow, Nimble
    Ring, Death Metal, Spear of Desolation, Spear of the Magus, Obsidian Shard, The
    Reaper, Tekko-Kagi, Heartseeker, Doom Orb, Lernaean Bow, The World Stone, Titan''s
    Bane, Tyrfing, The Crusher, Dreamer''s Idol, Hydra''s Lament, Bragi''s Harp, Avenging
    Blade, Toxic Blade, Bracer of The Abyss, Deathbringer, Chronos'' Pendant, Ancient
    Signet, Golden Blade, Pendulum Blade, Avatar''s Parashu, Dominance, Blood-Bound
    Book, The Cosmic Horror, The Executioner, Bancroft''s Talon, Musashi''s Dual Swords,
    Arondight, Oath-Sworn Spear, Demon Blade, Gem of Focus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.47
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.32
      fit: 0.56
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.13
      fit: 0.5
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Gluttonous Grimoire
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Silverbranch Bow, Death
    Metal, Soul Gem, Tyrfing, Spear of Desolation, Spear of the Magus, Obsidian Shard,
    Lernaean Bow, The Reaper, Tekko-Kagi, Bragi''s Harp, Hydra''s Lament, Bracer of
    The Abyss, Golden Blade, Heartseeker, Doom Orb, Chronos'' Pendant, Toxic Blade,
    Ancient Signet, The World Stone, Deathbringer, Dominance, Blood-Bound Book, Titan''s
    Bane, Dreamer''s Idol, The Crusher, Qin''s Blade, Bancroft''s Talon, Demon Blade,
    Gem of Focus, Musashi''s Dual Swords, Arondight, Transcendence, Rod of Asclepius,
    Runeforged Hammer, Book of Thoth, Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.3
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.52
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.65
      pick: 0.13
      fit: 0.46
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Nimble Ring, Spear of Desolation, Death Metal, Silverbranch Bow, Hydra''s
    Lament, Chronos'' Pendant, Spear of the Magus, Obsidian Shard, Lernaean Bow, The
    Reaper, Tyrfing, Tekko-Kagi, Arondight, Gem of Focus, Heartseeker, Bragi''s Harp,
    Bracer of The Abyss, Pendulum Blade, Doom Orb, Deathbringer, Ancient Signet, Golden
    Blade, The World Stone, Titan''s Bane, The Crusher, Dominance, Blood-Bound Book,
    Toxic Blade, Dreamer''s Idol, Totem of Death, Breastplate of Valor, Bancroft''s
    Talon, Musashi''s Dual Swords, Genji''s Guard, Demon Blade, Qin''s Blade, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.65
      pick: 0.13
      fit: 0.38
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.21
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death
    Metal, Soul Gem, Spear of Desolation, Spear of the Magus, Obsidian Shard, Lernaean
    Bow, Tyrfing, The Reaper, Silverbranch Bow, Tekko-Kagi, Bragi''s Harp, Hydra''s
    Lament, Heartseeker, Bracer of The Abyss, Deathbringer, Doom Orb, Golden Blade,
    Chronos'' Pendant, Titan''s Bane, The World Stone, Dominance, The Crusher, Ancient
    Signet, Blood-Bound Book, Dreamer''s Idol, Demon Blade, Toxic Blade, Musashi''s
    Dual Swords, Bancroft''s Talon, Arondight, Gem of Focus, Transcendence, Pendulum
    Blade, Runeforged Hammer, Avatar''s Parashu, Qin''s Blade, Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.38
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.29
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, Death Metal, Nimble Ring,
    The Reaper, Rod of Asclepius, Silverbranch Bow, Blood-Bound Book, Spear of Desolation,
    Spear of the Magus, Runeforged Hammer, Bancroft''s Talon, Obsidian Shard, Golden
    Blade, Ethereal Staff, Hydra''s Lament, Heartseeker, Lernaean Bow, Tyrfing, Tekko-Kagi,
    Bragi''s Harp, Deathbringer, Doom Orb, Yogi''s Necklace, Lifebinder, Chronos''
    Pendant, Toxic Blade, Jade Scepter, Avenging Blade, Titan''s Bane, The World Stone,
    Ancient Signet, Wish-Granting Pearl, The Crusher, Bracer of The Abyss, Dreamer''s
    Idol, Bloodforge, Daybreak Gavel, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.6
      win: 0.64
      pick: 0.32
      fit: 0.58
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.65
      pick: 0.13
      fit: 0.32
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Gluttonous Grimoire
  - Silverbranch Bow
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Soul Gem, Death Metal, Nimble Ring, The Reaper,
    Rod of Asclepius, Bancroft''s Talon, Blood-Bound Book, Spear of Desolation, Spear
    of the Magus, Hydra''s Lament, Runeforged Hammer, Silverbranch Bow, Obsidian Shard,
    Heartseeker, Ethereal Staff, Golden Blade, Ancient Signet, Lernaean Bow, Bragi''s
    Harp, Doom Orb, Wish-Granting Pearl, Tyrfing, The World Stone, Yogi''s Necklace,
    Chronos'' Pendant, Tekko-Kagi, Lifebinder, Deathbringer, Jade Scepter, Avenging
    Blade, Bracer of The Abyss, Titan''s Bane, The Crusher, Dominance, Transcendence,
    Dreamer''s Idol, Triton''s Conch, Daybreak Gavel.'
  slot_scores:
    Bancroft's Talon:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.52
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.23
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.33
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Musashi's Dual Swords
  - Deathbringer
  - Rod of Tahuti
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, Nimble Ring, Death Metal,
    The Reaper, Silverbranch Bow, Rod of Asclepius, Blood-Bound Book, Spear of Desolation,
    Spear of the Magus, Golden Blade, Bancroft''s Talon, Obsidian Shard, Runeforged
    Hammer, Ethereal Staff, Lernaean Bow, Tyrfing, Hydra''s Lament, Tekko-Kagi, Bragi''s
    Harp, Heartseeker, Toxic Blade, Bracer of The Abyss, Deathbringer, Doom Orb, Yogi''s
    Necklace, Chronos'' Pendant, Lifebinder, Jade Scepter, Ancient Signet, The World
    Stone, Wish-Granting Pearl, Berserker''s Shield, Avenging Blade, Titan''s Bane,
    Dreamer''s Idol, The Crusher, Daybreak Gavel, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.31
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.6
      win: 0.64
      pick: 0.32
      fit: 0.55
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.46
      win: 0.61
      pick: 0.0
      fit: 0.31
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, The Reaper, Nimble Ring, Death
    Metal, Spear of Desolation, Silverbranch Bow, Rod of Asclepius, Spear of the Magus,
    Obsidian Shard, Blood-Bound Book, Runeforged Hammer, Bancroft''s Talon, Hydra''s
    Lament, Heartseeker, Ethereal Staff, Golden Blade, Tekko-Kagi, Doom Orb, Lernaean
    Bow, Chronos'' Pendant, The World Stone, Titan''s Bane, Tyrfing, The Crusher,
    Toxic Blade, Dreamer''s Idol, Bragi''s Harp, Yogi''s Necklace, Lifebinder, Ancient
    Signet, Deathbringer, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Avenging
    Blade, Bracer of The Abyss, Pendulum Blade, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.12
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.12
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.6
      win: 0.64
      pick: 0.32
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Jotunn''s Revenge, The Reaper,
    Berserker''s Shield, Rod of Asclepius, Nimble Ring, Shield of the Phoenix, Death
    Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Bancroft''s Talon, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Runeforged Hammer, Spear of the Magus,
    Yogi''s Necklace, Spear of Desolation, Lifebinder, Helm of Radiance, Obsidian
    Shard, Golden Blade, Shifter''s Shield, Shield Splitter, Sphere of Negation, Hydra''s
    Lament, Chandra''s Grace, Phoenix Feather, Eye of the Storm, Heartseeker, Lernaean
    Bow, Erosion, Pharaoh''s Curse, Tyrfing, Jade Scepter, Umbral Link, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.28
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.6
      win: 0.64
      pick: 0.32
      fit: 0.51
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, The Reaper, Nimble Ring,
    Death Metal, Silverbranch Bow, Spear of the Magus, Spear of Desolation, Avenging
    Blade, Obsidian Shard, Rod of Asclepius, Blood-Bound Book, Heartseeker, Runeforged
    Hammer, Tekko-Kagi, Bancroft''s Talon, Doom Orb, Titan''s Bane, The World Stone,
    Golden Blade, Ethereal Staff, The Crusher, Toxic Blade, Hydra''s Lament, Dreamer''s
    Idol, Lernaean Bow, Tyrfing, Yogi''s Necklace, Bragi''s Harp, Deathbringer, Chronos''
    Pendant, Lifebinder, Ancient Signet, Jade Scepter, Wish-Granting Pearl, Bracer
    of The Abyss, Avatar''s Parashu, Pendulum Blade, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.12
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.13
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.6
      win: 0.64
      pick: 0.32
      fit: 0.65
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Gluttonous Grimoire
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, Nimble Ring, Silverbranch
    Bow, Death Metal, The Reaper, Rod of Asclepius, Golden Blade, Spear of the Magus,
    Spear of Desolation, Tyrfing, Blood-Bound Book, Obsidian Shard, Runeforged Hammer,
    Lernaean Bow, Toxic Blade, Bancroft''s Talon, Ethereal Staff, Tekko-Kagi, Bragi''s
    Harp, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Yogi''s Necklace, Doom
    Orb, Chronos'' Pendant, Lifebinder, Ancient Signet, Berserker''s Shield, Jade
    Scepter, Wish-Granting Pearl, The World Stone, Deathbringer, Dominance, Avenging
    Blade, Titan''s Bane, Dreamer''s Idol, Daybreak Gavel, The Crusher.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.12
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.69
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.65
      pick: 0.13
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.23
  community_ordered:
  - Riptalon
  - Silverbranch Bow
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Jotunn''s
    Revenge, Nimble Ring, Spear of Desolation, The Reaper, Death Metal, Hydra''s Lament,
    Rod of Asclepius, Silverbranch Bow, Blood-Bound Book, Chronos'' Pendant, Spear
    of the Magus, Chandra''s Grace, Bancroft''s Talon, Runeforged Hammer, Obsidian
    Shard, Golden Blade, Ethereal Staff, Arondight, Gem of Focus, Heartseeker, Lernaean
    Bow, Yogi''s Necklace, Tyrfing, Pendulum Blade, Toxic Blade, Tekko-Kagi, Shield
    of the Phoenix, Eye of Erebus, Doom Orb, Deathbringer, Lifebinder, Ancient Signet,
    Jade Scepter, Daybreak Gavel, The World Stone, Wish-Granting Pearl, Avenging Blade,
    Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.46
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.33
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.2
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Nimble Ring
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Soul Gem, Jotunn''s Revenge, Death Metal,
    Nimble Ring, The Reaper, Rod of Asclepius, Blood-Bound Book, Spear of Desolation,
    Spear of the Magus, Runeforged Hammer, Bancroft''s Talon, Obsidian Shard, Golden
    Blade, Ethereal Staff, Hydra''s Lament, Heartseeker, Lernaean Bow, Tyrfing, Silverbranch
    Bow, Tekko-Kagi, Bragi''s Harp, Deathbringer, Doom Orb, Yogi''s Necklace, Lifebinder,
    Chronos'' Pendant, Toxic Blade, Jade Scepter, Avenging Blade, Titan''s Bane, The
    World Stone, Ancient Signet, Wish-Granting Pearl, The Crusher, Daybreak Gavel,
    Bracer of The Abyss, Dreamer''s Idol, Bloodforge, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
---
